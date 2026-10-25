"""`GET /audit-log` -- HR/Admin review of audit entries."""

from fastapi import APIRouter, Query, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(tags=["audit-log"], dependencies=[Security(bearer_scheme)])


@router.get("/audit-log", response_model=StubResponse)
async def read_audit_log(
    employee_id: str | None = Query(default=None),
    from_: str | None = Query(default=None, alias="from"),
    to: str | None = Query(default=None),
) -> StubResponse:
    """Review audit entries for relevant employees."""
    return StubResponse(endpoint="GET /audit-log")
