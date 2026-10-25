"""`GET /me/...` -- the signed-in employee's own dashboard and hours."""

from fastapi import APIRouter, Query, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/me", tags=["me"], dependencies=[Security(bearer_scheme)])


@router.get("/dashboard", response_model=StubResponse)
async def dashboard() -> StubResponse:
    """Current shift status (clocked in/on break/out) and elapsed time."""
    return StubResponse(endpoint="GET /me/dashboard")


@router.get("/hours", response_model=StubResponse)
async def hours(
    from_: str | None = Query(default=None, alias="from"),
    to: str | None = Query(default=None),
) -> StubResponse:
    """Own daily and weekly totals with regular, overtime and break breakdown
    in local timezone."""
    return StubResponse(endpoint="GET /me/hours")
