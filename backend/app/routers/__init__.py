"""Generated routers: one per architecture component that owns endpoints.

`api_backend` owns every endpoint in the approved spec, grouped here by
resource rather than crammed into one module. `routers` is the list
`main.py` includes; add a new module and append it here when the spec grows.
"""

from app.routers import (
    audit,
    auth,
    clock,
    corrections,
    employees,
    export,
    me,
    privacy,
    records,
    settings,
    team,
)

routers = [
    auth.router,
    clock.router,
    me.router,
    team.router,
    corrections.router,
    employees.router,
    records.router,
    settings.router,
    export.router,
    privacy.router,
    audit.router,
]

__all__ = ["routers"]
