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
| [Architecture](architecture/README.md) | 5 entries |
| [Development](development/README.md) | 17 entries |
| [Testing](testing/README.md) | 0 entries |
| [Deployment](deployment/README.md) | 0 entries |
| [Maintenance](maintenance/README.md) | 0 entries |
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

- Human confirmation needed that the system truly never stores PHI, given the Healthcare industry tag -- this assumption underpins the decision to skip HIPAA-specific controls.
- No WCAG accessibility requirement is specified anywhere in requirements despite the Healthcare industry context; confirm whether accessibility compliance is required for any patient- or clinician-facing use.

### Architecture

- Architecture does not explicitly address WCAG accessibility implementation for the React SPA.

### Development

- Input does not specify which backlog items (stories/tasks) are assigned to this sprint; only the sprint goal and capacity were given, not an item-to-sprint mapping.
- No implementation/completion status (commits, PR merges, done/in-progress) was reported for any item in this epic -- plan only.
- No implementation/completion status was reported for any item in this epic -- plan only.
- No implementation/completion status was reported for this item -- plan only.
<!-- sdlc:auto:end open-gaps -->
