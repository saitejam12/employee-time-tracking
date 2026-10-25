"""`GET /export/timesheet.csv` -- the pay-period CSV timesheet for payroll."""

from fastapi import APIRouter, Query, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/export", tags=["export"], dependencies=[Security(bearer_scheme)])


@router.get("/timesheet.csv", response_model=StubResponse)
async def timesheet_csv(
    from_: str | None = Query(default=None, alias="from"),
    to: str | None = Query(default=None),
) -> StubResponse:
    """CSV timesheet for a pay period with per-employee regular, overtime,
    break and daily/weekly totals; overnight shifts on start day."""
    return StubResponse(endpoint="GET /export/timesheet.csv")
