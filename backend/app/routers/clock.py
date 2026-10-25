"""`POST /clock/...` -- clock-in/out and break start/stop.

Stubs only: US-004 (clock in/out) and US-005 (breaks) implement the open-shift
constraint, the break state machine and overnight-shift attribution.
"""

from fastapi import APIRouter, Security

from app.schemas import StubResponse
from app.security import bearer_scheme

router = APIRouter(prefix="/clock", tags=["clock"], dependencies=[Security(bearer_scheme)])


@router.post("/in", response_model=StubResponse)
async def clock_in() -> StubResponse:
    """Clock in and open a shift; blocked if a shift is open."""
    return StubResponse(endpoint="POST /clock/in")


@router.post("/out", response_model=StubResponse)
async def clock_out() -> StubResponse:
    """Clock out, auto-end any running break, compute worked duration."""
    return StubResponse(endpoint="POST /clock/out")


@router.post("/break/start", response_model=StubResponse)
async def break_start() -> StubResponse:
    """Start an unpaid break within the open shift."""
    return StubResponse(endpoint="POST /clock/break/start")


@router.post("/break/stop", response_model=StubResponse)
async def break_stop() -> StubResponse:
    """Stop the running break."""
    return StubResponse(endpoint="POST /clock/break/stop")
