# Traceability Matrix

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start legend -->
Built from recorded links, not written by a model: requirement key → plan item (`source_stable_key`) → development ticket (`stable_key`) → the ticket's test steps → the last live deployment that started after the work finished.
<!-- sdlc:auto:end legend -->

<!-- sdlc:auto:start matrix -->
| Requirement | Epic | Title | Plan items | Sprint | Design | Code | Commits | Ticket | Tests | Deployed |
|---|---|---|---|---|---|---|---|---|---|---|
| US-001 | EPIC-001 | Employee sign-in to own account | US-001 | 1 | GET /auth/me, POST /auth/login, api_backend, employees, web_frontend | — | — | not started | not run | — |
| US-002 | EPIC-001 | Password reset by email | US-002, US-002-T1, US-002-T2, US-002-T3, US-002-T4 | 2 | POST /auth/password-reset/confirm, POST /auth/password-reset/request, api_backend, database, email_service, employees, password_reset_tokens, web_frontend, worker | — | — | not started | not run | — |
| US-003 | EPIC-001 | Role-based access enforcement | US-003 | 1 | api_backend, employees, teams | — | — | not started | not run | — |
| US-004 | EPIC-002 | Clock in and out from a personal device | US-004 | 2 | POST /clock/in, POST /clock/out, api_backend, shifts, web_frontend | — | — | not started | not run | — |
| US-005 | EPIC-002 | Start and stop unpaid breaks within a shift | US-005 | 2 | POST /clock/break/start, POST /clock/break/stop, api_backend, breaks, shifts, web_frontend | — | — | not started | not run | — |
| US-006 | EPIC-002 | Record timestamps in the employee's timezone | US-006 | 3 | POST /clock/in, POST /clock/out, api_backend, database, employees, shifts | — | — | not started | not run | — |
| US-007 | EPIC-003 | Compute daily and weekly worked totals | US-007, US-007-T1, US-007-T2, US-007-T3, US-007-T4 | 3 | GET /me/hours, api_backend, breaks, daily_rollups, database, shifts, worker | — | — | not started | not run | — |
| US-008 | EPIC-003 | Split regular vs overtime hours | US-008 | 4 | GET /me/hours, api_backend, daily_rollups, database, org_settings | — | — | not started | not run | — |
| US-009 | EPIC-004 | View my daily and weekly hours | US-009 | 4 | GET /me/dashboard, GET /me/hours, api_backend, daily_rollups, web_frontend | — | — | not started | not run | — |
| US-010 | EPIC-005 | View team records and hours | US-010 | 4 | GET /team/records, api_backend, daily_rollups, shifts, teams, web_frontend | — | — | not started | not run | — |
| US-011 | EPIC-005 | See flagged missing or late entries | US-011 | 4 | GET /team/flags, api_backend, employees, shifts, web_frontend | — | — | not started | not run | — |
| US-012 | EPIC-005 | Manager clocks in for themselves | US-012 | 2 | POST /clock/in, POST /clock/out, api_backend, shifts | — | — | not started | not run | — |
| US-013 | EPIC-006 | Submit a correction request | US-013 | 5 | GET /corrections, POST /corrections, api_backend, correction_requests, web_frontend | — | — | not started | not run | — |
| US-014 | EPIC-006 | Approve or reject a correction request | US-014 | 5 | GET /team/corrections, POST /corrections/{id}/approve, POST /corrections/{id}/reject, api_backend, audit_log, correction_requests, shifts, web_frontend | — | — | not started | not run | — |
| US-015 | EPIC-007 | Notify on correction workflow events | US-015 | 5 | correction_requests, email_service, worker | — | — | not started | not run | — |
| US-016 | EPIC-007 | Optional missing clock-out reminder | US-016 | 6 | email_service, org_settings, shifts, worker | — | — | not started | not run | — |
| US-017 | EPIC-008 | Add and remove employees | US-017, US-017-T1, US-017-T2, US-017-T3, US-017-T4 | 1 | DELETE /employees/{id}, PATCH /employees/{id}, POST /employees, api_backend, database, employees, teams, web_frontend, worker | — | — | not started | not run | — |
| US-018 | EPIC-008 | Configure per-employee schedule and timezone | US-018 | 2 | PATCH /employees/{id}, api_backend, employees, web_frontend | — | — | not started | not run | — |
| US-019 | EPIC-008 | Edit any attendance record | US-019 | 5 | PATCH /records/{shift_id}, api_backend, audit_log, shifts, web_frontend | — | — | not started | not run | — |
| US-020 | EPIC-008 | Configure org-wide overtime thresholds | US-020 | 3 | GET /settings, PATCH /settings, api_backend, org_settings, web_frontend | — | — | not started | not run | — |
| US-021 | EPIC-009 | Export pay-period timesheet to CSV | US-021 | 6 | GET /export/timesheet.csv, api_backend, daily_rollups, shifts | — | — | not started | not run | — |
| US-022 | EPIC-010 | Access, export and delete personal data | US-022 | 6 | DELETE /privacy/{employee_id}, GET /privacy/{employee_id}/export, api_backend, audit_log, employees, shifts | — | — | not started | not run | — |
| US-023 | EPIC-010 | Audit log of edits, corrections and approvals | US-023 | 3 | GET /audit-log, api_backend, audit_log, database, web_frontend | — | — | not started | not run | — |
| US-024 | EPIC-010 | Encryption and standard availability | US-024 | 1 | api_backend, database | — | — | not started | not run | — |
<!-- sdlc:auto:end matrix -->
