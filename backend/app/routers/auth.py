"""`POST/GET /auth/...` -- sign-in, session profile, password reset, privacy ack.

Every handler is a stub: it returns `StubResponse` so the route exists, is
typed, and shows up in the OpenAPI document the frontend builds against,
before US-001/US-002 implement the real password check, JWT issuance and
token lifecycle.
"""

from fastapi import APIRouter, Body, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=StubResponse)
async def login(payload: dict = Body(default=None)) -> StubResponse:
    """Sign in with email and password; returns JWT or generic error."""
    return StubResponse(endpoint="POST /auth/login")


@router.get("/me", response_model=StubResponse, dependencies=[Security(bearer_scheme)])
async def read_me() -> StubResponse:
    """Current user profile, role, timezone and privacy-notice state."""
    return StubResponse(endpoint="GET /auth/me")


@router.post("/password-reset/request", response_model=StubResponse)
async def password_reset_request(payload: dict = Body(default=None)) -> StubResponse:
    """Request a reset link; always returns neutral confirmation, enqueues email."""
    return StubResponse(endpoint="POST /auth/password-reset/request")


@router.post("/password-reset/confirm", response_model=StubResponse)
async def password_reset_confirm(payload: dict = Body(default=None)) -> StubResponse:
    """Set a new password using a single-use time-limited token."""
    return StubResponse(endpoint="POST /auth/password-reset/confirm")


@router.post(
    "/privacy-notice/ack",
    response_model=StubResponse,
    dependencies=[Security(bearer_scheme)],
)
async def acknowledge_privacy_notice() -> StubResponse:
    """Record acknowledgement of the privacy notice at first sign-in."""
    return StubResponse(endpoint="POST /auth/privacy-notice/ack")
