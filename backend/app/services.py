"""The backing services this application is configured to reach.

Each entry maps a service to the environment variable that addresses it. The value
comes from docker-compose.yml through .env.example, so the health check reports
what the running deployment can actually reach.

`email-service` (SendGrid) has no key here yet -- the product owner supplies
`SENDGRID_API_KEY` before deployment. Code that sends mail must read it at the
point of use and disable itself with a clear message when it is empty, rather
than fail at startup; this map is only what `/health` reports is configured.
"""

import os

SERVICES = {
    "redis-queue": "REDIS_URL",
    "email-service": "SENDGRID_API_KEY",
}


def configured_services() -> dict[str, bool]:
    """Each service mapped to whether its connection variable is set."""
    return {name: bool(os.getenv(var)) for name, var in SERVICES.items()}
