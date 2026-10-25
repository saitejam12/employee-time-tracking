# Development

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start narrative -->
### DEV-PLAN-001 · approved · source: plan:v1

Approved development plan, version 1: 7 sprints of 20-point capacity each, sequencing the backlog from auth/sign-in through to privacy data rights.

- Sprint 1: employees can be provisioned and sign in; password reset works.
- Sprint 2: role-based access enforced, transport/at-rest encryption in place, employees can clock in/out.
- Sprint 3: breaks, per-employee timezone, schedule settings, overtime threshold configuration.
- Sprint 4: daily/weekly rollups, audit log, correction-request submission.
- Sprint 5: regular/overtime split, team records and missing/late flagging, HR record editing.
- Sprint 6: employees see own hours, managers approve/reject corrections, HR exports CSV timesheets.
- Sprint 7: correction-workflow emails, missing clock-out reminders, GDPR-style privacy data rights.

**Related:** EPIC-001, EPIC-002, EPIC-003, EPIC-004, EPIC-005, EPIC-006, EPIC-007, EPIC-008, EPIC-009, EPIC-010

- ⚠ The plan lists sprint goals and a separate backlog of epics/stories/tasks with points and assigned agent roles, but does not map specific backlog items to specific sprint numbers -- which items shipped in which sprint cannot be confirmed from this input.
- ⚠ No completion/status field (e.g. done, in-progress, blocked) was provided for any backlog item, so actual build progress against this plan is unknown.

### DEV-EPIC-001 · draft · source: plan:EPIC-001

Backlog breakdown for Authentication & Role-Based Access.

- US-001 Employee sign-in to own account (5 pts, backend-agent).
- US-002 Password reset by email (5 pts, backend-agent).
- US-003 Role-based access enforcement (8 pts, security-agent), with tasks: T1 role-based authorization dependency (security-agent), T2 team/org scoping on data-access endpoints (backend-agent), T3 cross-role access test suite (qa-agent).

**Related:** REQ-EPIC-001

- ⚠ No reported completion status for US-001/002/003 or their tasks.

### DEV-EPIC-002 · draft · source: plan:EPIC-002

Backlog breakdown for Clock In/Out & Breaks.

- US-004 Clock in/out from a personal device (8 pts, backend-agent), tasks: T1 shifts schema + open-shift constraint, T2 clock-in/out endpoints with overnight attribution (both backend-agent), T3 employee clock control UI (frontend-agent).
- US-005 Start/stop unpaid breaks (5 pts, backend-agent).
- US-006 Record timestamps in employee's timezone (5 pts, backend-agent).

**Related:** REQ-EPIC-002

- ⚠ No reported completion status for US-004/005/006 or their tasks.

### DEV-EPIC-003 · draft · source: plan:EPIC-003

Backlog breakdown for Worked Hours Computation & Overtime.

- US-007 Compute daily and weekly worked totals (8 pts, backend-agent), tasks: T1 daily_rollups schema, T2 daily worked-duration computation, T3 weekly aggregation from daily rollups (all backend-agent).
- US-008 Split regular vs overtime hours (5 pts, backend-agent).

**Related:** REQ-EPIC-003

- ⚠ No reported completion status for US-007/008 or their tasks.

### DEV-EPIC-004 · draft · source: plan:EPIC-004

Backlog breakdown for Personal Hours View.

- US-009 View my daily and weekly hours (5 pts, frontend-agent).

**Related:** REQ-EPIC-004

- ⚠ No reported completion status for US-009.

### DEV-EPIC-005 · draft · source: plan:EPIC-005

Backlog breakdown for Manager Team Oversight & Missing/Late Flagging.

- US-010 View team records and hours (5 pts, backend-agent).
- US-011 See flagged missing or late entries (5 pts, backend-agent).
- US-012 Manager clocks in for themselves (2 pts, backend-agent).

**Related:** REQ-EPIC-005

- ⚠ No reported completion status for US-010/011/012.

### DEV-EPIC-006 · draft · source: plan:EPIC-006

Backlog breakdown for the Correction Request Workflow.

- US-013 Submit a correction request (5 pts, backend-agent).
- US-014 Approve or reject a correction request (8 pts, backend-agent), tasks: T1 approve endpoint, T2 reject endpoint, T3 audit log entries for approve/reject (all backend-agent), T4 enqueue outcome notification job (integration-agent).

**Related:** REQ-EPIC-006

- ⚠ No reported completion status for US-013/014 or their tasks.

### DEV-EPIC-007 · draft · source: plan:EPIC-007

Backlog breakdown for Email Notifications.

- US-015 Notify on correction workflow events (8 pts, integration-agent), tasks: T1 stand up Redis-backed queue and arq worker service (devops-agent), T2 SendGrid templates for correction events (integration-agent), T3 wire correction endpoints to enqueue jobs (backend-agent), T4 log and swallow email delivery failures (backend-agent).
- US-016 Optional missing clock-out reminder (5 pts, integration-agent).

**Related:** REQ-EPIC-007

- ⚠ No reported completion status for US-015/016 or their tasks.

### DEV-EPIC-008 · draft · source: plan:EPIC-008

Backlog breakdown for HR/Admin Employee & Settings Management.

- US-017 Add and remove employees (8 pts, backend-agent), tasks: T1 employees/teams schema, T2 employee CRUD endpoints (backend-agent), T3 send invite email via SendGrid (integration-agent), T4 admin employee management screen (frontend-agent).
- US-018 Configure per-employee schedule and timezone (3 pts, backend-agent).
- US-019 Edit any attendance record (5 pts, backend-agent).
- US-020 Configure org-wide overtime thresholds (3 pts, backend-agent).

**Related:** REQ-EPIC-008

- ⚠ No reported completion status for US-017/018/019/020 or their tasks.

### DEV-EPIC-009 · draft · source: plan:EPIC-009

Backlog breakdown for CSV Timesheet Export.

- US-021 Export pay-period timesheet to CSV (5 pts, backend-agent).

**Related:** REQ-EPIC-009

- ⚠ No reported completion status for US-021.

### DEV-EPIC-010 · draft · source: plan:EPIC-010

Backlog breakdown for Privacy, Audit & Security.

- US-022 Access, export and delete personal data (5 pts, security-agent).
- US-023 Audit log of edits, corrections and approvals (5 pts, backend-agent).
- US-024 Encryption and standard availability (3 pts, devops-agent).

**Related:** REQ-EPIC-010

- ⚠ No reported completion status for US-022/023/024.
<!-- sdlc:auto:end narrative -->
