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
| [Development](development/README.md) | 1 entry |
| [Testing](testing/README.md) | 1 entry |
| [Deployment](deployment/README.md) | 1 entry |
| [Maintenance](maintenance/README.md) | 1 entry |
| [Data model](architecture/data-model.md) | generated |
| [API (OpenAPI)](architecture/api/openapi.yaml) | generated |
| [Decisions (ADRs)](architecture/adr/README.md) | 4 decisions |
| [Sprint plan](development/sprint-plan.md) | not generated yet |
| [Developer guide](development/developer-guide.md) | generated |
| [API reference](development/api-reference.md) | 1 route |
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

- Password policy criteria (length/complexity rules) referenced in AC-005/NFR-004 are not defined anywhere in the input.
- JWT/session expiry and system-logout mechanics (distinct from attendance clock-out) are not specified.
- Honour-system clock-in (NFR-015) is an accepted risk with no location/device verification — accuracy depends entirely on manager review and the correction workflow; confirm this residual risk is acceptable.
- The interaction between daily and weekly overtime thresholds (e.g., whether hours already counted as daily overtime are excluded from the weekly regular total to avoid double-counting) is not specified.
- Exact grace period (if any) before an employee is flagged late is not specified — AC-027 implies an immediate flag at expected start time with no stated tolerance window.
- The default/expected value for the 'reasonable window' before a missing clock-out reminder fires is not stated in requirements (architecture later models it as org_settings.reminder_window_hours with no default given).
- WCAG accessibility, called out by the healthcare domain skill for patient-facing apps, is not addressed anywhere for this internal staff tool — confirm whether an accessibility NFR is actually needed.
- No business-associate agreements (BAAs) are mentioned for vendors (SendGrid, AWS) despite the healthcare industry label; since no PHI is stored this may not be legally required, but should be confirmed with legal/compliance.
- HL7/FHIR/DICOM interoperability and FDA SaMD/EU MDR medical-device rules from the domain skill do not appear applicable since there is no EHR integration or clinical data — confirm this is intentionally out of scope rather than unaddressed.

### Architecture

- No observability/monitoring, log-retention, or backup/DR specifics are stated beyond 'encrypted at rest' and 'standard availability'.
- No API authentication token (JWT) expiry/refresh duration is specified.
- Architecture does not clarify whether daily-overtime hours are excluded from the weekly regular total before the 40h weekly threshold is applied (same double-counting ambiguity inherited from requirements, not resolved at the architecture level).
- JWT expiry/refresh strategy is not specified in the architecture input.

### Development

- Development phase has not started (or no implementation input was provided); there are no tickets, sprint plans, or code to document.

### Testing

- Testing phase has not started; no test strategy, cases, or results exist to document.

### Deployment

- No deployment recorded yet; nothing to document for actual releases, environments, or rollout status.

### Maintenance

- Maintenance phase not reached; no post-deployment notes exist to document.
<!-- sdlc:auto:end open-gaps -->
