"""The backing services this application is configured to reach.

Each entry maps a service to the environment variable that addresses it. The value
comes from docker-compose.yml through .env.example, so the health check reports
what the running deployment can actually reach.

`email-service` (SendGrid) has no key here yet -- the product owner supplies
`SENDGRID_API_KEY` before deployment. Code that sends mail must read it at the
point of use and disable itself with a clear message when it is empty, rather
than fail at startup; this map is only what `/health` reports is configured.
"""

import logging
import os

logger = logging.getLogger(__name__)

SERVICES = {
    "redis-queue": "REDIS_URL",
    "email-service": "SENDGRID_API_KEY",
}


def configured_services() -> dict[str, bool]:
    """Each service mapped to whether its connection variable is set."""
    return {name: bool(os.getenv(var)) for name, var in SERVICES.items()}


def send_password_reset_email(to_email: str, reset_link: str) -> None:
    """Send a password-reset link through SendGrid.

    A thin wrapper so callers (and tests) never touch the SendGrid SDK
    directly. With no `SENDGRID_API_KEY` configured this is a no-op that
    logs instead of sending, so tests and local runs need no network.
    """
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        logger.info("SendGrid not configured; skipping password reset email to %s", to_email)
        return

    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    message = Mail(
        from_email=os.getenv("SENDGRID_FROM_EMAIL", "no-reply@example.com"),
        to_emails=to_email,
        subject="Reset your password",
        plain_text_content=f"Use this link to reset your password: {reset_link}",
    )
    try:
        SendGridAPIClient(api_key).send(message)
    except Exception:  # pragma: no cover - network failure path, logged not raised
        logger.exception("Failed to send password reset email to %s", to_email)
