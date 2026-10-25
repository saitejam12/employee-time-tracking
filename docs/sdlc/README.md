# Small employee time-tracking web app — SDLC Documentation

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start overview -->
Build a small employee time-tracking web app. "Login/logout" here means
attendance clock-in and clock-out, not just signing into the system.

Who it's for:
- Employees: log into the web app from their own device and clock in when they
  start work and clock out when they finish. They can also start and stop unpaid
  breaks, and see their own daily and weekly hours.
- Managers: view their team's login/logout records and hours, spot missing or
  late entries, and approve correction requests.
- HR/Admin: add and remove employees, edit any record, and export timesheets.

Core behaviour it cannot ship without:
- Record a timestamp for each clock-in and clock-out per employee.
- Track break start/stop between clock-in and clock-out.
- Compute worked duration and roll it up per day and per week.
- Let an employee request a correction (e.g. forgot to clock out) and let their
  manager approve or reject it.

What it works with:
- Standalone. There is no HR or payroll integration. An admin creates the
  employee records inside the app.
- Timesheets export to CSV for payroll to consume manually.

Scale and constraints:
- One organisation, a small team (under ~50 employees).
- Web-based, each employee signs in with their own account.
- No hard launch deadline.
Build a small employee time-tracking web app. "Login/logout" here means
attendance clock-in and clock-out, not just signing into the system.

Who it's for:
- Employees: log into the web app from their own device and clock in when they
  start work and clock out when they finish. They can also start and stop unpaid
  breaks, and see their own daily and weekly hours.
- Managers: view their team's login/logout records and hours, spot missing or
  late entries, and approve correction requests.
- HR/Admin: add and remove employees, edit any record, and export timesheets.

Core behaviour it cannot ship without:
- Record a timestamp for each clock-in and clock-out per employee.
- Track break start/stop between clock-in and clock

**Documentation version:** v1
<!-- sdlc:auto:end overview -->

## Contents

<!-- sdlc:auto:start contents -->
| Document | State |
|---|---|
| [Requirements](requirements/README.md) | v1 approved |
| [Architecture](architecture/README.md) | 9 entries |
| [Development](development/README.md) | 11 entries |
| [Testing](testing/README.md) | 1 entry |
| [Deployment](deployment/README.md) | 1 entry |
| [Maintenance](maintenance/README.md) | 1 entry |
| [Data model](architecture/data-model.md) | generated |
| [API (OpenAPI)](architecture/api/openapi.yaml) | generated |
| [Decisions (ADRs)](architecture/adr/README.md) | 4 decisions |
| [Sprint plan](development/sprint-plan.md) | 7 sprints |
| [Developer guide](development/developer-guide.md) | not generated yet |
| [API reference](development/api-reference.md) | 0 routes |
| [Test report](testing/test-report.md) | not run yet |
| [Deployment guide](deployment/deployment-guide.md) | not deployed yet |
| [Runbook](deployment/runbook.md) | not deployed yet |
| [Release notes](deployment/release-notes.md) | 0 releases |
| [Traceability matrix](traceability-matrix.md) | 24 requirements |
| [Changelog](CHANGELOG.md) | 1 version |
<!-- sdlc:auto:end contents -->

## Open gaps

<!-- sdlc:auto:start open-gaps -->
### Requirements

- Concrete password complexity/length policy referenced by AC-005/NFR-004 is not defined in the input.
- The 'no PHI / not a medical device' classification is asserted in the requirements but not shown as confirmed by a compliance/legal reviewer -- recommend explicit human sign-off given the project is tagged Healthcare industry (see top-level gaps).

### Architecture

- No explicit AWS region or data-residency configuration is specified, despite the stated mixed-region GDPR-style rationale for choosing AWS -- flagged for formalisation as the org grows.
- No explicit region, backup/retention schedule, or disaster-recovery target is stated for RDS/ElastiCache beyond 'standard availability'.

### Development

- The plan lists sprint goals and a separate backlog of epics/stories/tasks with points and assigned agent roles, but does not map specific backlog items to specific sprint numbers -- which items shipped in which sprint cannot be confirmed from this input.
- No completion/status field (e.g. done, in-progress, blocked) was provided for any backlog item, so actual build progress against this plan is unknown.
- No reported completion status for US-001/002/003 or their tasks.
- No reported completion status for US-004/005/006 or their tasks.
- No reported completion status for US-007/008 or their tasks.
- No reported completion status for US-009.
- No reported completion status for US-010/011/012.
- No reported completion status for US-013/014 or their tasks.
- No reported completion status for US-015/016 or their tasks.
- No reported completion status for US-017/018/019/020 or their tasks.
- No reported completion status for US-021.
- No reported completion status for US-022/023/024.

### Testing

- Testing phase has not started: no test plans, test cases, execution results, coverage data, or defect records were provided.

### Deployment

- No deployment recorded yet: no release, environment promotion, or rollout/rollback history was provided, despite an approved deployment architecture (ARCH-008) existing.

### Maintenance

- No maintenance phase input: no incidents, monitoring data, support tickets, or patch history were provided, consistent with no deployment having occurred yet.
<!-- sdlc:auto:end open-gaps -->
