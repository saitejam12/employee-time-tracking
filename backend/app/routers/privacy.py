"""`/privacy/{employee_id}...` -- GDPR-style subject-rights operations."""

from fastapi import APIRouter, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/privacy", tags=["privacy"], dependencies=[Security(bearer_scheme)])


@router.get("/{employee_id}/export", response_model=StubResponse)
async def export_personal_data(employee_id: str) -> StubResponse:
    """Generate a personal-data export (identity + attendance) for an access request."""
    return StubResponse(endpoint="GET /privacy/{employee_id}/export")


@router.delete("/{employee_id}", response_model=StubResponse)
async def delete_personal_data(employee_id: str) -> StubResponse:
    """Delete or irreversibly anonymise an employee's personal data; recorded
    in audit log."""
    return StubResponse(endpoint="DELETE /privacy/{employee_id}")
