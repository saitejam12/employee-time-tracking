"""`GET /team/...` -- a manager's view of their team's records, flags and
pending correction requests."""

from fastapi import APIRouter, Query, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/team", tags=["team"], dependencies=[Security(bearer_scheme)])


@router.get("/records", response_model=StubResponse)
async def team_records(
    from_: str | None = Query(default=None, alias="from"),
    to: str | None = Query(default=None),
) -> StubResponse:
    """Manager view of team members' clock events and rolled-up hours for a period."""
    return StubResponse(endpoint="GET /team/records")


@router.get("/flags", response_model=StubResponse)
async def team_flags(date: str | None = Query(default=None)) -> StubResponse:
    """Team members flagged missing/late or under expected hours."""
    return StubResponse(endpoint="GET /team/flags")


@router.get("/corrections", response_model=StubResponse)
async def team_corrections(status: str | None = Query(default=None)) -> StubResponse:
    """Pending correction requests for the manager's team."""
    return StubResponse(endpoint="GET /team/corrections")
