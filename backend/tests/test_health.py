"""The baseline test the scaffold ships with.

The platform installs this tree and runs `pytest` against it, so there has to
be something green to run before an agent has written anything -- otherwise the
first real ticket cannot tell a broken change from a repository that never
worked.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_reports_ok() -> None:
    """A failure here means the application does not import or does not start."""
    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert set(body["services"]) == {"redis-queue", "email-service"}


def test_the_openapi_document_builds() -> None:
    """Every generated route contributes to the schema, so a route whose types
    FastAPI cannot resolve fails here rather than on a user's first request."""
    response = client.get("/openapi.json")

    assert response.status_code == 200
    paths = response.json()["paths"]
    assert "/health" in paths
    # One stub per endpoint the approved API spec declares (see
    # docs/sdlc/architecture/api/openapi.yaml), so a route that fails to wire
    # up is caught here rather than discovered by the first ticket that needs it.
    for path in [
        "/auth/login",
        "/auth/me",
        "/auth/password-reset/request",
        "/auth/password-reset/confirm",
        "/auth/privacy-notice/ack",
        "/clock/in",
        "/clock/out",
        "/clock/break/start",
        "/clock/break/stop",
        "/me/dashboard",
        "/me/hours",
        "/team/records",
        "/team/flags",
        "/team/corrections",
        "/corrections",
        "/corrections/{id}/approve",
        "/corrections/{id}/reject",
        "/employees",
        "/employees/{id}",
        "/records/{shift_id}",
        "/settings",
        "/export/timesheet.csv",
        "/privacy/{employee_id}/export",
        "/privacy/{employee_id}",
        "/audit-log",
    ]:
        assert path in paths, f"missing {path}"
