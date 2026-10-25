"""POST /auth/password-reset/{request,confirm} and the reset-token lifecycle
(US-002, acceptance AC-004/AC-005, NFR-004).

No network call ever leaves this process: `sendgrid.SendGridAPIClient.send` is
patched out everywhere a token needs to be read, so the suite never talks to
SendGrid, and the token is read back out of the (fake) dispatched email
rather than guessed at from the DB's hash.

PENDING note: see test_auth.py -- `app/routers/auth.py` is still a stub as of
this run, so these assertions describe the contract the implementation must
meet rather than a defect already observed in working code.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

from app import models

SENDGRID_SEND = "sendgrid.SendGridAPIClient.send"


def _fake_sendgrid_response():
    response = MagicMock()
    response.status_code = 202
    return response


def _extract_token(call_args) -> str:
    assert call_args is not None, "password-reset/request did not dispatch any email"
    args, kwargs = call_args
    message = args[0] if args else kwargs.get("message")
    payload = message.get() if hasattr(message, "get") else message
    text = payload if isinstance(payload, str) else json.dumps(payload, default=str)
    match = re.search(r"token=([A-Za-z0-9\-_.]+)", text)
    assert match, f"could not find a reset token in the dispatched email body: {text!r}"
    return match.group(1)


def test_reset_request_is_neutral_and_only_emails_the_registered_address(
    client, employee_factory
):
    """AC-004."""
    employee_factory(email="dora@example.com", password="CorrectHorse9!")

    with patch(SENDGRID_SEND, return_value=_fake_sendgrid_response()) as mock_send:
        resp_registered = client.post(
            "/auth/password-reset/request", json={"email": "dora@example.com"}
        )
        calls_after_registered = mock_send.call_count

        resp_unregistered = client.post(
            "/auth/password-reset/request", json={"email": "nobody@example.com"}
        )
        calls_after_unregistered = mock_send.call_count

    assert resp_registered.status_code == resp_unregistered.status_code
    assert resp_registered.json() == resp_unregistered.json(), (
        "the response must be identical whether or not the email is registered"
    )
    assert calls_after_registered == 1, "the registered email must trigger exactly one send"
    assert calls_after_unregistered == calls_after_registered, (
        "an unregistered email must not dispatch any mail"
    )


def test_reset_token_lifecycle(client, employee_factory):
    """AC-005, NFR-004: valid token sets a compliant password that then logs in;
    a policy-violating password is rejected; reusing the token afterwards fails."""
    employee_factory(email="erin@example.com", password="OldPassword9!")

    with patch(SENDGRID_SEND, return_value=_fake_sendgrid_response()) as mock_send:
        client.post("/auth/password-reset/request", json={"email": "erin@example.com"})
        token = _extract_token(mock_send.call_args)

    weak_resp = client.post(
        "/auth/password-reset/confirm", json={"token": token, "new_password": "short"}
    )
    assert weak_resp.status_code in (400, 422), "a policy-violating password must be rejected"

    good_resp = client.post(
        "/auth/password-reset/confirm",
        json={"token": token, "new_password": "NewCompliantPass1"},
    )
    assert good_resp.status_code == 200

    login_resp = client.post(
        "/auth/login", json={"email": "erin@example.com", "password": "NewCompliantPass1"}
    )
    assert login_resp.status_code == 200, "the newly-set password must sign in"

    reuse_resp = client.post(
        "/auth/password-reset/confirm",
        json={"token": token, "new_password": "AnotherCompliant1"},
    )
    assert reuse_resp.status_code in (400, 401, 410), "a used token must not work twice"


def test_expired_reset_token_is_rejected(client, db_session, employee_factory):
    """AC-005."""
    employee = employee_factory(email="frank@example.com", password="OldPassword9!")

    with patch(SENDGRID_SEND, return_value=_fake_sendgrid_response()) as mock_send:
        client.post("/auth/password-reset/request", json={"email": "frank@example.com"})
        token = _extract_token(mock_send.call_args)

    row = (
        db_session.query(models.PasswordResetToken)
        .filter_by(employee_id=employee.id)
        .order_by(models.PasswordResetToken.id.desc())
        .first()
    )
    assert row is not None, "password-reset/request did not persist a token row"
    row.expires_at = datetime.now(timezone.utc) - timedelta(hours=1)
    db_session.commit()

    resp = client.post(
        "/auth/password-reset/confirm",
        json={"token": token, "new_password": "NewCompliantPass1"},
    )
    assert resp.status_code in (400, 401, 410), "an expired token must be rejected"
