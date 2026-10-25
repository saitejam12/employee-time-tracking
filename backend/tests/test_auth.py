"""POST /auth/login, GET /auth/me and the no-self-signup guarantee (US-001).

PENDING note: as of this run `app/routers/auth.py` is still the generated
stub (`StubResponse` on every route), so every assertion below currently
fails against real behaviour rather than confirming a defect in it -- these
are written against the approved contract (openapi.yaml, SignIn.tsx, api.ts)
for the implementation to land against, per the concurrent-build process.
"""

from __future__ import annotations

import uuid

import jwt

from app import models


def test_login_returns_token_with_role_and_team_claims_and_me_matches(client, db_session, employee_factory):
    """AC-001."""
    team = models.Team(id=uuid.uuid4(), name="Ops")
    db_session.add(team)
    db_session.commit()

    employee = employee_factory(
        email="alice@example.com", password="CorrectHorse9!", role="manager", team_id=team.id
    )

    response = client.post(
        "/auth/login", json={"email": "alice@example.com", "password": "CorrectHorse9!"}
    )
    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token, "login response must carry an access_token"

    # Decoded without verifying the signature: this test asserts on the claims'
    # shape, not on the implementation's choice of signing secret.
    claims = jwt.decode(token, options={"verify_signature": False})
    assert claims.get("role") == "manager", f"token claims missing/wrong role: {claims}"
    assert claims.get("team") == str(team.id) or claims.get("team_id") == str(
        team.id
    ), f"token claims missing/wrong team: {claims}"

    me = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == 200
    me_body = me.json()
    assert me_body.get("email") == "alice@example.com" or me_body.get("id") == str(employee.id)


def test_unknown_email_wrong_password_and_deactivated_all_look_identical(
    client, employee_factory
):
    """AC-002, NFR-003: a failed sign-in must never reveal which part was wrong."""
    employee_factory(email="bob@example.com", password="CorrectHorse9!", is_active=True)
    employee_factory(email="carol@example.com", password="CorrectHorse9!", is_active=False)

    resp_unknown = client.post(
        "/auth/login", json={"email": "nobody@example.com", "password": "whatever123"}
    )
    resp_wrong_password = client.post(
        "/auth/login", json={"email": "bob@example.com", "password": "WrongPassword1"}
    )
    resp_deactivated = client.post(
        "/auth/login", json={"email": "carol@example.com", "password": "CorrectHorse9!"}
    )

    responses = [resp_unknown, resp_wrong_password, resp_deactivated]
    statuses = {r.status_code for r in responses}
    assert len(statuses) == 1, f"status codes differ between failure reasons: {statuses}"

    bodies = {r.text for r in responses}
    assert len(bodies) == 1, (
        "response bodies differ between unknown-email / wrong-password / deactivated -- "
        "this leaks which credential was wrong"
    )


def test_openapi_exposes_no_self_signup_route(client):
    """AC-003."""
    paths = client.get("/openapi.json").json()["paths"]

    forbidden_markers = ("signup", "sign-up", "register")
    leaked = [p for p in paths if any(marker in p.lower() for marker in forbidden_markers)]
    assert not leaked, f"self-signup/registration route(s) exposed: {leaked}"

    # Employee provisioning exists, but only for an authenticated admin, never a
    # public self-registration route.
    assert "/employees" in paths
    assert paths["/employees"].get("post", {}).get("security"), (
        "/employees POST must require auth -- it is the admin-only provisioning route, "
        "not public self-signup"
    )
