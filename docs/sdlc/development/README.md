# Development

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start narrative -->
### DEV-PLAN-001 · approved · source: plan:v1

Development plan version 1 is approved, organised into 6 sprints of 20-point capacity each, covering authentication through CSV export and GDPR-style data rights.

Plan status: approved, version 1. Six sprints were defined, each with a capacity of 20 points: Sprint 1 - admin-provisioned accounts, sign-in, RBAC and baseline encryption; Sprint 2 - clock in/out with unpaid breaks, password reset by email, per-employee schedule/timezone settings; Sprint 3 - timezone-correct timestamps, daily/weekly rollups, overtime thresholds, audit log; Sprint 4 - regular/overtime split, personal and team hours views, missing/late flagging; Sprint 5 - correction request workflow, manager approvals, HR record edits, related email notifications; Sprint 6 - missing clock-out reminders, CSV payroll export, GDPR-style data access/export/delete. The backlog beneath this plan contains 10 epics and 24 stories (US-001 through US-024) plus supporting tasks.

**Related:** US-001, US-002, US-003, US-004, US-005, US-006, US-007, US-008, US-009, US-010, US-011, US-012, US-013, US-014, US-015, US-016, US-017, US-018, US-019, US-020, US-021, US-022, US-023, US-024

- ⚠ No explicit mapping is provided of which backlog items (US-xxx) were assigned to which sprint number -- only thematic overlap between sprint goals and epics can be inferred.
- ⚠ No record of actual sprint execution, velocity achieved, or whether sprints completed as planned.

### DEV-SPRINT-1 · approved · source: plan:Sprint 1

Sprint 1 goal: admin-provisioned accounts, sign-in, role-based access control and baseline encryption.

Goal: 'Admin-provisioned accounts, sign-in, role-based access control and baseline encryption.' Capacity: 20 points. Thematically aligns with EPIC-001 (Authentication & Role-Based Access) and the encryption portion of US-024.

**Related:** US-001, US-002, US-003, US-024

- ⚠ No explicit item-to-sprint assignment given; alignment to EPIC-001/US-024 is inferred from goal wording only.
- ⚠ No completion or acceptance record for this sprint.

### DEV-SPRINT-2 · approved · source: plan:Sprint 2

Sprint 2 goal: clock in/out with unpaid breaks, password reset by email, and per-employee schedule/timezone settings.

Goal: 'Clock in/out with unpaid breaks, password reset by email, and per-employee schedule/timezone settings.' Capacity: 20 points. Thematically aligns with US-004, US-005 (EPIC-002), US-002 (password reset), and US-018 (schedule/timezone settings).

**Related:** US-004, US-005, US-002, US-018

- ⚠ No explicit item-to-sprint assignment given; alignment is inferred from goal wording only.
- ⚠ No completion or acceptance record for this sprint.

### DEV-SPRINT-3 · approved · source: plan:Sprint 3

Sprint 3 goal: timezone-correct timestamps, daily/weekly worked-hour rollups, overtime thresholds and the audit log.

Goal: 'Timezone-correct timestamps, daily/weekly worked-hour rollups, overtime thresholds and the audit log.' Capacity: 20 points. Thematically aligns with US-006, US-007 (and its tasks), US-008, US-020 (overtime thresholds) and US-023 (audit log).

**Related:** US-006, US-007, US-008, US-020, US-023

- ⚠ No explicit item-to-sprint assignment given; alignment is inferred from goal wording only.
- ⚠ No completion or acceptance record for this sprint.

### DEV-SPRINT-4 · approved · source: plan:Sprint 4

Sprint 4 goal: regular/overtime split, personal and team hours views, and missing/late flagging.

Goal: 'Regular/overtime split, personal and team hours views, and missing/late flagging.' Capacity: 20 points. Thematically aligns with US-008, US-009 (EPIC-004), US-010, US-011, US-012 (EPIC-005).

**Related:** US-008, US-009, US-010, US-011, US-012

- ⚠ No explicit item-to-sprint assignment given; alignment is inferred from goal wording only.
- ⚠ No completion or acceptance record for this sprint.

### DEV-SPRINT-5 · approved · source: plan:Sprint 5

Sprint 5 goal: correction request workflow, manager approvals, HR record edits and related email notifications.

Goal: 'Correction request workflow, manager approvals, HR record edits and related email notifications.' Capacity: 20 points. Thematically aligns with US-013, US-014 (EPIC-006), US-019 (HR record edits) and US-015 (notification emails).

**Related:** US-013, US-014, US-019, US-015

- ⚠ No explicit item-to-sprint assignment given; alignment is inferred from goal wording only.
- ⚠ No completion or acceptance record for this sprint.

### DEV-SPRINT-6 · approved · source: plan:Sprint 6

Sprint 6 goal: missing clock-out reminders, CSV payroll export, and GDPR-style data access/export/delete.

Goal: 'Missing clock-out reminders, CSV payroll export, and GDPR-style data access/export/delete.' Capacity: 20 points. Thematically aligns with US-016 (reminder), US-021 (EPIC-009 CSV export) and US-022 (EPIC-010 privacy rights).

**Related:** US-016, US-021, US-022

- ⚠ No explicit item-to-sprint assignment given; alignment is inferred from goal wording only.
- ⚠ No completion or acceptance record for this sprint.

### EPIC-001 · approved · source: plan:EPIC-001

Authentication & Role-Based Access epic: employee sign-in, password reset, and role-based access enforcement.

Epic has no points/role assigned at the epic level (grouping only). Contains: 1) US-001 Employee sign-in to own account (5 pts, backend-agent). 2) US-002 Password reset by email (8 pts, integration-agent), broken into: US-002-T1 add password_reset_tokens table and token generation/validation (backend-agent); US-002-T2 implement reset request/confirm endpoints with neutral messaging (backend-agent); US-002-T3 send reset email via Redis queue and SendGrid (integration-agent); US-002-T4 build forgot-password and reset-password screens (frontend-agent). 3) US-003 Role-based access enforcement (5 pts, security-agent).

**Related:** US-001, US-002, US-003

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.

### EPIC-002 · approved · source: plan:EPIC-002

Clock In/Out & Breaks epic: recording attendance timestamps and unpaid break tracking per shift.

Epic has no points/role assigned at the epic level. Contains: 1) US-004 Clock in and out from a personal device (5 pts, backend-agent). 2) US-005 Start and stop unpaid breaks within a shift (3 pts, backend-agent). 3) US-006 Record timestamps in the employee's timezone (3 pts, backend-agent).

**Related:** US-004, US-005, US-006

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.

### EPIC-003 · approved · source: plan:EPIC-003

Worked Hours Computation & Overtime epic: daily/weekly totals and regular-vs-overtime split.

Epic has no points/role assigned at the epic level. Contains: 1) US-007 Compute daily and weekly worked totals (8 pts, backend-agent), broken into: US-007-T1 design daily_rollups schema with overnight-shift attribution rule; US-007-T2 implement worked-duration computation service; US-007-T3 implement weekly aggregation from daily rollups; US-007-T4 add rollup recomputation trigger on shift/break changes (all backend-agent). 2) US-008 Split regular vs overtime hours (5 pts, backend-agent).

**Related:** US-007, US-008

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.
- ⚠ Overnight-shift attribution rule referenced in US-007-T1 is not itself defined in the input -- its specifics are undocumented.

### EPIC-004 · approved · source: plan:EPIC-004

Personal Hours View epic: lets an employee see their own daily and weekly worked hours.

Epic has no points/role assigned at the epic level. Contains: 1) US-009 View my daily and weekly hours (5 pts, frontend-agent).

**Related:** US-009

- ⚠ No completion status, code review, or test evidence provided for this epic.

### EPIC-005 · approved · source: plan:EPIC-005

Manager Team Oversight & Missing/Late Flagging epic: team record visibility and attendance exception flags.

Epic has no points/role assigned at the epic level. Contains: 1) US-010 View team records and hours (5 pts, frontend-agent). 2) US-011 See flagged missing or late entries (5 pts, backend-agent). 3) US-012 Manager clocks in for themselves (1 pt, backend-agent).

**Related:** US-010, US-011, US-012

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.

### EPIC-006 · approved · source: plan:EPIC-006

Correction Request Workflow epic: employees submit corrections, managers approve or reject them.

Epic has no points/role assigned at the epic level. Contains: 1) US-013 Submit a correction request (5 pts, backend-agent). 2) US-014 Approve or reject a correction request (5 pts, backend-agent).

**Related:** US-013, US-014

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.

### EPIC-007 · approved · source: plan:EPIC-007

Email Notifications epic: notifications for correction workflow events and an optional missing clock-out reminder.

Epic has no points/role assigned at the epic level. Contains: 1) US-015 Notify on correction workflow events (5 pts, integration-agent). 2) US-016 Optional missing clock-out reminder (3 pts, integration-agent).

**Related:** US-015, US-016

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.
- ⚠ 'Optional' nature of the missing clock-out reminder (US-016) is not elaborated -- unclear whether it is a per-org or per-employee toggle.

### EPIC-008 · approved · source: plan:EPIC-008

HR/Admin Employee & Settings Management epic: add/remove employees, edit records, and configure schedules and overtime thresholds.

Epic has no points/role assigned at the epic level. Contains: 1) US-017 Add and remove employees (8 pts, backend-agent), broken into: US-017-T1 add employees and teams schema with invite token support; US-017-T2 implement employee create/update/deactivate endpoints (both backend-agent); US-017-T3 send invite email via background worker on employee creation (integration-agent); US-017-T4 build HR admin screen to add and deactivate employees (frontend-agent). 2) US-018 Configure per-employee schedule and timezone (3 pts, backend-agent). 3) US-019 Edit any attendance record (5 pts, backend-agent). 4) US-020 Configure org-wide overtime thresholds (3 pts, backend-agent).

**Related:** US-017, US-018, US-019, US-020

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.

### EPIC-009 · approved · source: plan:EPIC-009

CSV Timesheet Export epic: lets HR/Admin export pay-period timesheets to CSV for payroll.

Epic has no points/role assigned at the epic level. Contains: 1) US-021 Export pay-period timesheet to CSV (5 pts, backend-agent).

**Related:** US-021

- ⚠ No completion status, code review, or test evidence provided for this epic.
- ⚠ CSV column/format specification is not given in the input.

### EPIC-010 · approved · source: plan:EPIC-010

Privacy, Audit & Security epic: personal data access/export/delete, an audit log, and encryption/availability baselines.

Epic has no points/role assigned at the epic level. Contains: 1) US-022 Access, export and delete personal data (5 pts, security-agent). 2) US-023 Audit log of edits, corrections and approvals (5 pts, backend-agent). 3) US-024 Encryption and standard availability (2 pts, devops-agent).

**Related:** US-022, US-023, US-024

- ⚠ No completion status, code review, or test evidence provided for any item in this epic.
- ⚠ No named regulation (e.g. GDPR) or specific compliance standard was supplied with the input despite the 'GDPR-style' phrasing used in the project description, so compliance coverage cannot be formally traced here.

### DEV-STATUS-001 · draft

Overall development execution status is undocumented for this phase.

The input supplied is a backlog/sprint plan (scope, points, role ownership) with plan status 'approved, version 1'. It contains no information on which items are in progress, done, blocked, or deferred; no commit, pull-request, or build references; and no developer-reported notes or test outcomes.

- ⚠ No ticket/item completion status provided for any of the 24 stories or their sub-tasks.
- ⚠ No code artifacts, PR links, or commit history provided.
- ⚠ No indication of whether Sprint 1-6 dates have actually occurred or are still pending.
<!-- sdlc:auto:end narrative -->
