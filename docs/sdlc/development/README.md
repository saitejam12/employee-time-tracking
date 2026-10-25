# Development

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start narrative -->
### DEV-SPRINT-1 · approved · source: plan:Sprint 1

Sprint 1 goal: employees can be provisioned and can sign in; password reset works. Capacity: 20 points.

Plan status: approved, version 1. Goal: 'Employees can be provisioned and can sign in; password reset works.' Capacity: 20 points.

- ⚠ Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.

### DEV-SPRINT-2 · approved · source: plan:Sprint 2

Sprint 2 goal: role-based access is enforced, transport/at-rest encryption is in place, and employees can clock in/out. Capacity: 20 points.

Plan status: approved, version 1. Goal: 'Role-based access is enforced, transport/at-rest encryption is in place, and employees can clock in/out.' Capacity: 20 points.

- ⚠ Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.

### DEV-SPRINT-3 · approved · source: plan:Sprint 3

Sprint 3 goal: breaks, per-employee timezone, schedule settings and overtime threshold configuration are in place. Capacity: 20 points.

Plan status: approved, version 1. Goal: 'Breaks, per-employee timezone, schedule settings and overtime threshold configuration are in place.' Capacity: 20 points.

- ⚠ Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.

### DEV-SPRINT-4 · approved · source: plan:Sprint 4

Sprint 4 goal: daily/weekly worked-hour rollups, the audit log, and correction-request submission are live. Capacity: 20 points.

Plan status: approved, version 1. Goal: 'Daily/weekly worked-hour rollups, the audit log, and correction-request submission are live.' Capacity: 20 points.

- ⚠ Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.

### DEV-SPRINT-5 · approved · source: plan:Sprint 5

Sprint 5 goal: regular/overtime split, team records and missing/late flagging, and HR record editing are live. Capacity: 20 points.

Plan status: approved, version 1. Goal: 'Regular/overtime split, team records and missing/late flagging, and HR record editing are live.' Capacity: 20 points.

- ⚠ Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.

### DEV-SPRINT-6 · approved · source: plan:Sprint 6

Sprint 6 goal: employees see their own hours, managers can approve/reject corrections, and HR can export CSV timesheets. Capacity: 20 points.

Plan status: approved, version 1. Goal: 'Employees see their own hours, managers can approve/reject corrections, and HR can export CSV timesheets.' Capacity: 20 points.

- ⚠ Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.

### DEV-SPRINT-7 · approved · source: plan:Sprint 7

Sprint 7 goal: correction-workflow emails, missing clock-out reminders, and GDPR-style privacy data rights are live. Capacity: 20 points.

Plan status: approved, version 1. Goal: 'Correction-workflow emails, missing clock-out reminders, and GDPR-style privacy data rights are live.' Capacity: 20 points.

- ⚠ Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.

### DEV-EPIC-001 · approved · source: dev:EPIC-001

Backlog for Authentication & Role-Based Access: 3 stories and 3 sub-tasks covering sign-in, password reset, and RBAC enforcement.

US-001 [story] Employee sign-in to own account (5 pts, backend-agent). US-002 [story] Password reset by email (5 pts, backend-agent). US-003 [story] Role-based access enforcement (8 pts, security-agent), with US-003-T1 Implement role-based authorization dependency in API backend (security-agent), US-003-T2 Apply team/org scoping to data-access endpoints (backend-agent), US-003-T3 Add cross-role access test suite (qa-agent).

**Related:** REQ-EPIC-001, US-001, US-002, US-003, US-003-T1, US-003-T2, US-003-T3

- ⚠ No implementation/completion status (commits, PR merges, done/in-progress) was reported for any item in this epic -- plan only.

### DEV-EPIC-002 · approved · source: dev:EPIC-002

Backlog for Clock In/Out & Breaks: 3 stories, with the clock-in/out story broken into schema, endpoint, and UI tasks.

US-004 [story] Clock in and out from a personal device (8 pts, backend-agent), with US-004-T1 Add shifts schema and open-shift constraint (backend-agent), US-004-T2 Implement clock-in/clock-out endpoints with overnight attribution (backend-agent), US-004-T3 Build employee clock control UI (frontend-agent). US-005 [story] Start and stop unpaid breaks within a shift (5 pts, backend-agent). US-006 [story] Record timestamps in the employee's timezone (5 pts, backend-agent).

**Related:** REQ-EPIC-002, US-004, US-004-T1, US-004-T2, US-004-T3, US-005, US-006

- ⚠ No implementation/completion status was reported for any item in this epic -- plan only.

### DEV-EPIC-003 · approved · source: dev:EPIC-003

Backlog for Worked Hours Computation & Overtime: daily/weekly rollup story plus overtime-split story.

US-007 [story] Compute daily and weekly worked totals (8 pts, backend-agent), with US-007-T1 Add daily_rollups schema, US-007-T2 Implement daily worked-duration computation, US-007-T3 Implement weekly aggregation from daily rollups (all backend-agent). US-008 [story] Split regular vs overtime hours (5 pts, backend-agent).

**Related:** REQ-EPIC-003, US-007, US-007-T1, US-007-T2, US-007-T3, US-008

- ⚠ No implementation/completion status was reported for any item in this epic -- plan only.

### DEV-EPIC-004 · approved · source: dev:EPIC-004

Backlog for Personal Hours View: single frontend story.

US-009 [story] View my daily and weekly hours (5 pts, frontend-agent).

**Related:** REQ-EPIC-004, US-009

- ⚠ No implementation/completion status was reported for this item -- plan only.

### DEV-EPIC-005 · approved · source: dev:EPIC-005

Backlog for Manager Team Oversight & Missing/Late Flagging: 3 backend stories.

US-010 [story] View team records and hours (5 pts, backend-agent). US-011 [story] See flagged missing or late entries (5 pts, backend-agent). US-012 [story] Manager clocks in for themselves (2 pts, backend-agent).

**Related:** REQ-EPIC-005, US-010, US-011, US-012

- ⚠ No implementation/completion status was reported for any item in this epic -- plan only.

### DEV-EPIC-006 · approved · source: dev:EPIC-006

Backlog for Correction Request Workflow: submission story plus approve/reject story broken into endpoint, audit, and notification tasks.

US-013 [story] Submit a correction request (5 pts, backend-agent). US-014 [story] Approve or reject a correction request (8 pts, backend-agent), with US-014-T1 Implement correction approve endpoint, US-014-T2 Implement correction reject endpoint, US-014-T3 Write audit log entries for approve/reject (backend-agent), and US-014-T4 Enqueue outcome notification job (integration-agent).

**Related:** REQ-EPIC-006, US-013, US-014, US-014-T1, US-014-T2, US-014-T3, US-014-T4

- ⚠ No implementation/completion status was reported for any item in this epic -- plan only.

### DEV-EPIC-007 · approved · source: dev:EPIC-007

Backlog for Email Notifications: correction-event notification story (with queue/worker, template, wiring and failure-handling tasks) plus optional reminder story.

US-015 [story] Notify on correction workflow events (8 pts, integration-agent), with US-015-T1 Stand up Redis-backed queue and arq worker service (devops-agent), US-015-T2 Build SendGrid email templates for correction events (integration-agent), US-015-T3 Wire correction endpoints to enqueue notification jobs (backend-agent), US-015-T4 Log and swallow email delivery failures (backend-agent). US-016 [story] Optional missing clock-out reminder (5 pts, integration-agent).

**Related:** REQ-EPIC-007, US-015, US-015-T1, US-015-T2, US-015-T3, US-015-T4, US-016

- ⚠ No implementation/completion status was reported for any item in this epic -- plan only.

### DEV-EPIC-008 · approved · source: dev:EPIC-008

Backlog for HR/Admin Employee & Settings Management: employee CRUD story (with schema, endpoints, invite email, and admin UI tasks), plus schedule/timezone, record-edit, and threshold-configuration stories.

US-017 [story] Add and remove employees (8 pts, backend-agent), with US-017-T1 Add employees/teams schema (backend-agent), US-017-T2 Implement employee CRUD endpoints (backend-agent), US-017-T3 Send invite email via SendGrid (integration-agent), US-017-T4 Build admin employee management screen (frontend-agent). US-018 [story] Configure per-employee schedule and timezone (3 pts, backend-agent). US-019 [story] Edit any attendance record (5 pts, backend-agent). US-020 [story] Configure org-wide overtime thresholds (3 pts, backend-agent).

**Related:** REQ-EPIC-008, US-017, US-017-T1, US-017-T2, US-017-T3, US-017-T4, US-018, US-019, US-020

- ⚠ No implementation/completion status was reported for any item in this epic -- plan only.

### DEV-EPIC-009 · approved · source: dev:EPIC-009

Backlog for CSV Timesheet Export: single backend story.

US-021 [story] Export pay-period timesheet to CSV (5 pts, backend-agent).

**Related:** REQ-EPIC-009, US-021

- ⚠ No implementation/completion status was reported for this item -- plan only.

### DEV-EPIC-010 · approved · source: dev:EPIC-010

Backlog for Privacy, Audit & Security: subject-rights story, audit-log story, and encryption/availability story.

US-022 [story] Access, export and delete personal data (5 pts, security-agent). US-023 [story] Audit log of edits, corrections and approvals (5 pts, backend-agent). US-024 [story] Encryption and standard availability (3 pts, devops-agent).

**Related:** REQ-EPIC-010, US-022, US-023, US-024

- ⚠ No implementation/completion status was reported for any item in this epic -- plan only.
<!-- sdlc:auto:end narrative -->
