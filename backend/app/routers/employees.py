"""`/employees...` -- HR/Admin provisioning, editing and deactivation."""

from fastapi import APIRouter, Body, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/employees", tags=["employees"], dependencies=[Security(bearer_scheme)])


@router.post("", response_model=StubResponse)
async def create_employee(payload: dict = Body(default=None)) -> StubResponse:
    """Create an admin-provisioned employee and send an invite/reset link."""
    return StubResponse(endpoint="POST /employees")


@router.patch("/{id}", response_model=StubResponse)
async def update_employee(id: str, payload: dict = Body(default=None)) -> StubResponse:
    """Edit employee identity, role, team, timezone and schedule."""
    return StubResponse(endpoint="PATCH /employees/{id}")


@router.delete("/{id}", response_model=StubResponse)
async def deactivate_employee(id: str) -> StubResponse:
    """Deactivate an employee; sign-in blocked, records retained."""
    return StubResponse(endpoint="DELETE /employees/{id}")
