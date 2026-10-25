"""Application entrypoint.

Generated from the approved architecture: one router per component that owns
endpoints, one route per endpoint the API spec declares. Every generated route
is a stub that returns a typed placeholder, so the service starts, serves its
OpenAPI document and passes its tests before a single handler is implemented.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models  # noqa: F401 -- imported so the tables register before create_all
from app.database import Base, engine
from app.routers import routers
from app.services import configured_services

app = FastAPI(
    title="Small employee time-tracking web app",
    description="Build a small employee time-tracking web app. \"Login/logout\" here means\nattendance clock-in and clock-out, not just signing into the system.\n\nWho it's for:\n- Employees: log into the web app from their own device and clock in when they\n  start work and clock out when they finish. They can also start and stop unpaid\n  breaks, and see their own daily and weekly hours.\n- Managers: view their team's login/logout records and hours, spot missing or\n  late entries, and approve correction requests.\n- HR/Admin: add and remove employees, edit any record, and export timesheets.\n\nCore behaviour it cannot ship without:\n- Record a timestamp for each clock-in and clock-out per employee.\n- Track break start/stop between clock-in and clock-out.\n- Compute worked duration and roll it up per day and per week.\n- Let an employee request a correction (e.g. forgot to clock out) and let their\n  manager approve or reject it.\n\nWhat it works with:\n- Standalone. There is no HR or payroll integration. An admin creates the\n  employee records inside the app.\n- Timesheets export to CSV for payroll to consume manually.\n\nScale and constraints:\n- One organisation, a small team (under ~50 employees).\n- Web-based, each employee signs in with their own account.\n- No hard launch deadline.\nBuild a small employee time-tracking web app. \"Login/logout\" here means\nattendance clock-in and clock-out, not just signing into the system.\n\nWho it's for:\n- Employees: log into the web app from their own device and clock in when they\n  start work and clock out when they finish. They can also start and stop unpaid\n  breaks, and see their own daily and weekly hours.\n- Managers: view their team's login/logout records and hours, spot missing or\n  late entries, and approve correction requests.\n- HR/Admin: add and remove employees, edit any record, and export timesheets.\n\nCore behaviour it cannot ship without:\n- Record a timestamp for each clock-in and clock-out per employee.\n- Track break start/stop between clock-in and clock",
    version="0.1.0",
)

# The SPA runs on a different origin than the API, so the browser refuses its calls
# unless that origin is allowed here. In development that is the Vite dev server; when
# deployed, the platform injects the frontend's real URL as ALLOWED_ORIGINS (comma
# separated). Point ALLOWED_ORIGINS at the real thing and nothing else has to change.
_dev_origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
_allowed_origins = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins or _dev_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# The scaffold ships no migrations, so the tables are created from the models on
# startup. Replace this with Alembic before anything holds data worth keeping.
Base.metadata.create_all(bind=engine)

for _router in routers:
    app.include_router(_router)


@app.get("/health")
async def health() -> dict[str, object]:
    """Liveness probe, and the only route here that is not a stub."""
    return {"status": "ok", "services": configured_services()}
