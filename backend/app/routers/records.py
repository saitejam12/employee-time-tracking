"""`PATCH /records/{shift_id}` -- HR/Admin correction of any clock record."""

from fastapi import APIRouter, Body, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/records", tags=["records"], dependencies=[Security(bearer_scheme)])


@router.patch("/{shift_id}", response_model=StubResponse)
async def update_record(shift_id: str, payload: dict = Body(default=None)) -> StubResponse:
    """HR/Admin edit any clock or break times; recompute totals, audit."""
    return StubResponse(endpoint="PATCH /records/{shift_id}")
