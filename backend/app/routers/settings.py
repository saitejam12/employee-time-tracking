"""`/settings` -- org-wide overtime thresholds and reminder configuration."""

from fastapi import APIRouter, Body, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/settings", tags=["settings"], dependencies=[Security(bearer_scheme)])


@router.get("", response_model=StubResponse)
async def read_settings() -> StubResponse:
    """View org-wide overtime thresholds and reminder settings."""
    return StubResponse(endpoint="GET /settings")


@router.patch("", response_model=StubResponse)
async def update_settings(payload: dict = Body(default=None)) -> StubResponse:
    """Change thresholds/reminder settings; triggers org-wide recompute."""
    return StubResponse(endpoint="PATCH /settings")
