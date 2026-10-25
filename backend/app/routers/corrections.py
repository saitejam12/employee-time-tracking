"""`/corrections...` -- an employee's own correction requests, and a
manager's approve/reject decision on one."""

from fastapi import APIRouter, Body, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(
    prefix="/corrections", tags=["corrections"], dependencies=[Security(bearer_scheme)]
)


@router.post("", response_model=StubResponse)
async def submit_correction(payload: dict = Body(default=None)) -> StubResponse:
    """Employee submits a correction request; saved pending, manager emailed."""
    return StubResponse(endpoint="POST /corrections")


@router.get("", response_model=StubResponse)
async def list_own_corrections() -> StubResponse:
    """Own correction requests and their status."""
    return StubResponse(endpoint="GET /corrections")


@router.post("/{id}/approve", response_model=StubResponse)
async def approve_correction(id: str) -> StubResponse:
    """Approve a team correction; update record, recompute totals, audit, email."""
    return StubResponse(endpoint="POST /corrections/{id}/approve")


@router.post("/{id}/reject", response_model=StubResponse)
async def reject_correction(id: str, payload: dict = Body(default=None)) -> StubResponse:
    """Reject a team correction with a reason; audit, email."""
    return StubResponse(endpoint="POST /corrections/{id}/reject")
