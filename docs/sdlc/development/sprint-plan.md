# Sprint Plan

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start sprints -->
## Sprint 1: Sprint 1

Employees can be provisioned and can sign in; password reset works.

Capacity: 20 points · Committed: 18

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-001 | Story | Employee sign-in to own account | 5 | backend-agent | US-017 |
| US-002 | Story | Password reset by email | 5 | backend-agent | US-001 |
| US-017 | Story | Add and remove employees | 8 | backend-agent | — |
| ↳ US-017-T1 | Task | Add employees/teams schema | — | backend-agent | — |
| ↳ US-017-T2 | Task | Implement employee CRUD endpoints | — | backend-agent | — |
| ↳ US-017-T3 | Task | Send invite email via SendGrid | — | integration-agent | — |
| ↳ US-017-T4 | Task | Build admin employee management screen | — | frontend-agent | — |

## Sprint 2: Sprint 2

Role-based access is enforced, transport/at-rest encryption is in place, and employees can clock in/out.

Capacity: 20 points · Committed: 19

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-003 | Story | Role-based access enforcement | 8 | security-agent | US-001 |
| ↳ US-003-T1 | Task | Implement role-based authorization dependency in API backend | — | security-agent | — |
| ↳ US-003-T2 | Task | Apply team/org scoping to data-access endpoints | — | backend-agent | — |
| ↳ US-003-T3 | Task | Add cross-role access test suite | — | qa-agent | — |
| US-004 | Story | Clock in and out from a personal device | 8 | backend-agent | US-001 |
| ↳ US-004-T1 | Task | Add shifts schema and open-shift constraint | — | backend-agent | — |
| ↳ US-004-T2 | Task | Implement clock-in/clock-out endpoints with overnight attribution | — | backend-agent | — |
| ↳ US-004-T3 | Task | Build employee clock control UI | — | frontend-agent | — |
| US-024 | Story | Encryption and standard availability | 3 | devops-agent | — |

## Sprint 3: Sprint 3

Breaks, per-employee timezone, schedule settings and overtime threshold configuration are in place.

Capacity: 20 points · Committed: 18

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-005 | Story | Start and stop unpaid breaks within a shift | 5 | backend-agent | US-004 |
| US-006 | Story | Record timestamps in the employee's timezone | 5 | backend-agent | US-004 |
| US-012 | Story | Manager clocks in for themselves | 2 | backend-agent | US-004 |
| US-018 | Story | Configure per-employee schedule and timezone | 3 | backend-agent | US-017 |
| US-020 | Story | Configure org-wide overtime thresholds | 3 | backend-agent | — |

## Sprint 4: Sprint 4

Daily/weekly worked-hour rollups, the audit log, and correction-request submission are live.

Capacity: 20 points · Committed: 18

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-007 | Story | Compute daily and weekly worked totals | 8 | backend-agent | US-004, US-005, US-006 |
| ↳ US-007-T1 | Task | Add daily_rollups schema | — | backend-agent | — |
| ↳ US-007-T2 | Task | Implement daily worked-duration computation | — | backend-agent | — |
| ↳ US-007-T3 | Task | Implement weekly aggregation from daily rollups | — | backend-agent | — |
| US-013 | Story | Submit a correction request | 5 | backend-agent | US-004, US-003 |
| US-023 | Story | Audit log of edits, corrections and approvals | 5 | backend-agent | US-003 |

## Sprint 5: Sprint 5

Regular/overtime split, team records and missing/late flagging, and HR record editing are live.

Capacity: 20 points · Committed: 20

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-008 | Story | Split regular vs overtime hours | 5 | backend-agent | US-007 |
| US-010 | Story | View team records and hours | 5 | backend-agent | US-007, US-008, US-003 |
| US-011 | Story | See flagged missing or late entries | 5 | backend-agent | US-010, US-018 |
| US-019 | Story | Edit any attendance record | 5 | backend-agent | US-004, US-023 |

## Sprint 6: Sprint 6

Employees see their own hours, managers can approve/reject corrections, and HR can export CSV timesheets.

Capacity: 20 points · Committed: 18

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-009 | Story | View my daily and weekly hours | 5 | frontend-agent | US-007, US-008 |
| US-014 | Story | Approve or reject a correction request | 8 | backend-agent | US-013, US-023 |
| ↳ US-014-T1 | Task | Implement correction approve endpoint | — | backend-agent | — |
| ↳ US-014-T2 | Task | Implement correction reject endpoint | — | backend-agent | — |
| ↳ US-014-T3 | Task | Write audit log entries for approve/reject | — | backend-agent | — |
| ↳ US-014-T4 | Task | Enqueue outcome notification job | — | integration-agent | — |
| US-021 | Story | Export pay-period timesheet to CSV | 5 | backend-agent | US-007, US-008 |

## Sprint 7: Sprint 7

Correction-workflow emails, missing clock-out reminders, and GDPR-style privacy data rights are live.

Capacity: 20 points · Committed: 18

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-015 | Story | Notify on correction workflow events | 8 | integration-agent | US-013, US-014 |
| ↳ US-015-T1 | Task | Stand up Redis-backed queue and arq worker service | — | devops-agent | — |
| ↳ US-015-T2 | Task | Build SendGrid email templates for correction events | — | integration-agent | — |
| ↳ US-015-T3 | Task | Wire correction endpoints to enqueue notification jobs | — | backend-agent | — |
| ↳ US-015-T4 | Task | Log and swallow email delivery failures | — | backend-agent | — |
| US-016 | Story | Optional missing clock-out reminder | 5 | integration-agent | US-015 |
| US-022 | Story | Access, export and delete personal data | 5 | security-agent | US-017, US-023 |

## Unscheduled

_Nothing unscheduled._
<!-- sdlc:auto:end sprints -->
