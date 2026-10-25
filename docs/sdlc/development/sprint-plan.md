# Sprint Plan

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start sprints -->
## Sprint 1: Sprint 1

Admin-provisioned accounts, sign-in, role-based access control and baseline encryption.

Capacity: 20 points · Committed: 20

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-001 | Story | Employee sign-in to own account | 5 | backend-agent | US-017 |
| US-003 | Story | Role-based access enforcement | 5 | security-agent | US-001, US-017 |
| US-017 | Story | Add and remove employees | 8 | backend-agent | — |
| ↳ US-017-T1 | Task | Add employees and teams schema with invite token support | — | backend-agent | — |
| ↳ US-017-T2 | Task | Implement employee create/update/deactivate endpoints | — | backend-agent | — |
| ↳ US-017-T3 | Task | Send invite email via background worker on employee creation | — | integration-agent | — |
| ↳ US-017-T4 | Task | Build HR admin screen to add and deactivate employees | — | frontend-agent | — |
| US-024 | Story | Encryption and standard availability | 2 | devops-agent | — |

## Sprint 2: Sprint 2

Clock in/out with unpaid breaks, password reset by email, and per-employee schedule/timezone settings.

Capacity: 20 points · Committed: 20

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-002 | Story | Password reset by email | 8 | integration-agent | US-001 |
| ↳ US-002-T1 | Task | Add password_reset_tokens table and token generation/validation | — | backend-agent | — |
| ↳ US-002-T2 | Task | Implement reset request/confirm endpoints with neutral messaging | — | backend-agent | — |
| ↳ US-002-T3 | Task | Send reset email via Redis queue and SendGrid | — | integration-agent | — |
| ↳ US-002-T4 | Task | Build forgot-password and reset-password screens | — | frontend-agent | — |
| US-004 | Story | Clock in and out from a personal device | 5 | backend-agent | US-001 |
| US-005 | Story | Start and stop unpaid breaks within a shift | 3 | backend-agent | US-004 |
| US-012 | Story | Manager clocks in for themselves | 1 | backend-agent | US-004 |
| US-018 | Story | Configure per-employee schedule and timezone | 3 | backend-agent | US-017 |

## Sprint 3: Sprint 3

Timezone-correct timestamps, daily/weekly worked-hour rollups, overtime thresholds and the audit log.

Capacity: 20 points · Committed: 19

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-006 | Story | Record timestamps in the employee's timezone | 3 | backend-agent | US-004, US-018 |
| US-007 | Story | Compute daily and weekly worked totals | 8 | backend-agent | US-005, US-006 |
| ↳ US-007-T1 | Task | Design daily_rollups schema with overnight-shift attribution rule | — | backend-agent | — |
| ↳ US-007-T2 | Task | Implement worked-duration computation service | — | backend-agent | — |
| ↳ US-007-T3 | Task | Implement weekly aggregation from daily rollups | — | backend-agent | — |
| ↳ US-007-T4 | Task | Add rollup recomputation trigger on shift/break changes | — | backend-agent | — |
| US-020 | Story | Configure org-wide overtime thresholds | 3 | backend-agent | US-017 |
| US-023 | Story | Audit log of edits, corrections and approvals | 5 | backend-agent | US-017 |

## Sprint 4: Sprint 4

Regular/overtime split, personal and team hours views, and missing/late flagging.

Capacity: 20 points · Committed: 20

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-008 | Story | Split regular vs overtime hours | 5 | backend-agent | US-007, US-020 |
| US-009 | Story | View my daily and weekly hours | 5 | frontend-agent | US-007, US-008 |
| US-010 | Story | View team records and hours | 5 | frontend-agent | US-008, US-003 |
| US-011 | Story | See flagged missing or late entries | 5 | backend-agent | US-010, US-018 |

## Sprint 5: Sprint 5

Correction request workflow, manager approvals, HR record edits and related email notifications.

Capacity: 20 points · Committed: 20

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-013 | Story | Submit a correction request | 5 | backend-agent | US-004 |
| US-014 | Story | Approve or reject a correction request | 5 | backend-agent | US-013, US-023 |
| US-015 | Story | Notify on correction workflow events | 5 | integration-agent | US-013, US-014, US-002 |
| US-019 | Story | Edit any attendance record | 5 | backend-agent | US-023, US-007 |

## Sprint 6: Sprint 6

Missing clock-out reminders, CSV payroll export, and GDPR-style data access/export/delete.

Capacity: 20 points · Committed: 13

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-016 | Story | Optional missing clock-out reminder | 3 | integration-agent | US-004, US-015 |
| US-021 | Story | Export pay-period timesheet to CSV | 5 | backend-agent | US-007, US-008 |
| US-022 | Story | Access, export and delete personal data | 5 | security-agent | US-017, US-023 |

## Unscheduled

_Nothing unscheduled._
<!-- sdlc:auto:end sprints -->
