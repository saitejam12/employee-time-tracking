# API Reference

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start endpoints -->
| Method | Path | Handler | Source | Summary |
|---|---|---|---|---|
| GET | /health | health | `backend/app/main.py:43` | Liveness probe, and the only route here that is not a stub. |
<!-- sdlc:auto:end endpoints -->

<!-- sdlc:auto:start drift -->
**Designed but missing:**

- DELETE /employees/{id}
- DELETE /privacy/{employee_id}
- GET /audit-log
- GET /auth/me
- GET /corrections
- GET /export/timesheet.csv
- GET /me/dashboard
- GET /me/hours
- GET /privacy/{employee_id}/export
- GET /settings
- GET /team/corrections
- GET /team/flags
- GET /team/records
- PATCH /employees/{id}
- PATCH /records/{shift_id}
- PATCH /settings
- POST /auth/login
- POST /auth/password-reset/confirm
- POST /auth/password-reset/request
- POST /auth/privacy-notice/ack
- POST /clock/break/start
- POST /clock/break/stop
- POST /clock/in
- POST /clock/out
- POST /corrections
- POST /corrections/{id}/approve
- POST /corrections/{id}/reject
- POST /employees
<!-- sdlc:auto:end drift -->

<!-- sdlc:auto:start source -->
Generated from commit `59df5bc`
<!-- sdlc:auto:end source -->
