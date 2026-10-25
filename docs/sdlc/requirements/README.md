# Product Requirements

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start narrative -->
## Summary

### REQ-EPIC-001 · draft · source: requirements:EPIC-001

Admin-provisioned email/password sign-in, self-service password reset, and strict role-based access control across Employee, Manager, and HR/Admin roles. No self-signup is permitted.

US-001 (critical): employee signs in with email+password from any device and lands on a personal dashboard with clock controls and hours (AC-001); wrong credentials get one generic 'invalid credentials' message without indicating which field was wrong (AC-002); no self-signup option exists, accounts are admin-provisioned only (AC-003). US-002 (high): user requests a reset from the sign-in page; a time-limited link is emailed to the registered address with a neutral confirmation shown regardless of whether the email exists (AC-004); setting a new password meeting the policy updates the account and the link becomes single-use (AC-005). US-003 (critical): employees see only their own data (AC-006); managers see their team plus themselves (AC-007); HR/Admin see and edit org-wide (AC-008). NFR-001 enforces role-based need-to-know access; NFR-002 confirms admin-only provisioning via invite/reset links; NFR-003/NFR-004 define safe failure messaging and single-use, time-limited reset tokens.

**Related:** US-001, US-002, US-003, NFR-001, NFR-002, NFR-003, NFR-004

### REQ-EPIC-002 · draft · source: requirements:EPIC-002

Employees clock in/out from any personal device on the honour system (no geofencing/kiosk/biometric) and take unpaid breaks inside an open shift; timestamps use the employee's configured timezone and overnight shifts are supported.

US-004 (critical): Clock In records a timestamp and opens the shift (AC-009); Clock Out records a timestamp, closes the shift, and computes worked duration (AC-010); Clock In is unavailable while a shift is open, preventing overlap (AC-011); a shift starting before midnight and ending after it is attributed to its start day (AC-012). US-005 (high): Start Break records a break-start timestamp (AC-013); Stop Break records break-end and subtracts break time from worked duration (AC-014); an in-progress break is auto-ended or the user is prompted at clock-out, and break time is never counted as worked (AC-015). US-006 (high): clock events are stored and displayed in the employee's configured timezone; day boundaries for rollups use that timezone (AC-016). NFR-015 is an accepted risk: honour-system clock-in with no geofencing/kiosk/biometric, relying on manager review and corrections for accuracy. NFR-012 requires clock actions to stay instant (emails run in background).

**Related:** US-004, US-005, US-006, NFR-012, NFR-015

### REQ-EPIC-003 · draft · source: requirements:EPIC-003

Computes worked duration per shift excluding unpaid breaks, rolls it up per day and per week, and splits regular vs overtime hours against admin-configurable thresholds defaulting to 8h/day and 40h/week.

US-007 (critical): daily total equals the sum of (clock-out minus clock-in minus unpaid breaks) for shifts attributed to that day (AC-017); weekly total equals the sum of daily totals for the week (AC-018). US-008 (high): at the 8h/day default, 10h worked yields 8h regular + 2h overtime (AC-019); weekly hours beyond the 40h default are overtime (AC-020); changing thresholds recomputes the regular/overtime split org-wide (AC-021).

**Related:** US-007, US-008

### REQ-EPIC-004 · draft · source: requirements:EPIC-004

Employees can view their own daily and weekly hours, broken into regular/overtime/break time, plus their current shift status.

US-009 (high): the hours view shows per-day/per-week regular, overtime and break hours in the employee's timezone (AC-022); the dashboard shows current shift status (clocked in / on break / clocked out) and elapsed time (AC-023); employees can see only their own hours, not any other employee's (AC-024).

**Related:** US-009

### REQ-EPIC-005 · draft · source: requirements:EPIC-005

Managers view their team's attendance records and hours, see missing/late and under-expected-hours flags, and clock in/out themselves as ordinary employees.

US-010 (high): manager sees each team member's clock events and daily/weekly hours (regular, overtime, break) for a selected period (AC-025), restricted to their own assigned team (AC-026). US-011 (high): an employee is flagged missing/late if not clocked in by their expected start time (AC-027); a day is flagged under-expected-hours if worked time falls below the employee's standard daily hours (AC-028). US-012 (medium): managers clock in/out and take breaks on their own employee account, tracked identically to any employee (AC-029).

**Related:** US-010, US-011, US-012

### REQ-EPIC-006 · draft · source: requirements:EPIC-006

Employees request corrections to their records (e.g. a forgotten clock-out); the relevant manager approves or rejects, driving the audit trail and email notifications.

US-013 (high): employee submits proposed times plus a reason; the request is saved pending and the manager is emailed (AC-030); the employee can view the request's status as pending, approved, or rejected (AC-031). US-014 (high): manager approval updates the affected record, recomputes totals, emails the employee, and writes an audit entry (AC-032); manager rejection with a reason leaves the record unchanged, emails the employee with the reason, and writes an audit entry (AC-033).

**Related:** US-013, US-014

### REQ-EPIC-007 · draft · source: requirements:EPIC-007

Transactional email notifications cover correction-submitted (to manager), correction approved/rejected (to employee), and an optional missing-clock-out reminder.

US-015 (medium): manager is emailed when a correction is submitted (AC-034); employee is emailed the decision, including the reason if rejected (AC-035); if the email provider isn't configured, the in-app action still completes and the failure is logged rather than blocking the workflow (AC-036, NFR-011). US-016 (low): if reminders are enabled by an admin and a shift stays open beyond the configured window, the employee receives a reminder email prompting a clock-out or correction request (AC-037); no email is sent when the feature is disabled (AC-038).

**Related:** US-015, US-016, NFR-011

### REQ-EPIC-008 · draft · source: requirements:EPIC-008

HR/Admin provision and deactivate employee accounts, set per-employee schedule/timezone, edit any attendance record, and configure org-wide overtime thresholds.

US-017 (critical): HR/Admin creates an employee with name/email/role/team; the employee sets a password via an emailed invite/reset link (AC-039); deactivation blocks sign-in while historical records are retained for reporting unless removed via a privacy request (AC-040, NFR-008). US-018 (high): HR/Admin sets each employee's timezone, expected start time, and standard daily hours, which drive their rollups and missing/late flags (AC-041). US-019 (high): HR/Admin edits any clock or break time; totals recompute and the change is captured in the audit log with actor, before/after values, and timestamp (AC-042). US-020 (medium): overtime thresholds default to 8h/day and 40h/week (AC-043); changes apply org-wide to rollups and exports (AC-044). NFR-002 confirms accounts are admin-provisioned only, no self-signup.

**Related:** US-017, US-018, US-019, US-020, NFR-002, NFR-008

### REQ-EPIC-009 · draft · source: requirements:EPIC-009

HR/Admin exports a CSV timesheet for a selected pay period for manual payroll use; there is no direct payroll integration.

US-021 (high): CSV includes per-employee regular hours, overtime hours, break time, and daily/weekly totals for the selected date range (AC-045); overnight shifts are counted on their start day, consistent with in-app rollups (AC-046); the org-wide export is restricted to HR/Admin and unavailable to managers or employees (AC-047).

**Related:** US-021

### REQ-EPIC-010 · draft · source: requirements:EPIC-010

GDPR-style privacy baseline for mixed-region staff: role-limited access, a privacy notice, subject-rights access/export/delete, a full audit log, encryption in transit and at rest, and explicitly standard (non-clinical) availability.

US-022 (medium): HR/Admin can generate an export of an employee's identity+attendance data for an access request (AC-048); can delete or irreversibly anonymise personal data for an approved erasure request, recorded in the audit log (AC-049); employees see a privacy notice explaining stored data and its purpose at first sign-in (AC-050). US-023 (high): every record edit, correction submission, approval, or rejection writes an audit entry with actor, action, affected record, before/after values, and timestamp (AC-051); HR/Admin can review the log (AC-052). US-024 (medium): browser-server traffic is HTTPS/TLS encrypted (AC-053); data is encrypted at rest (AC-054); standard, non-clinical-grade availability applies and no payment/billing functionality exists (AC-055, NFR-010 accepted risk). NFR-006: GDPR-style subject rights. NFR-007: the system stores only minimal attendance+identity data, explicitly no PHI, and is not a clinical/medical-device system. NFR-009: privacy notice shown at first sign-in. Compliance trace: the industry tag is Healthcare, but this requirement set explicitly states no PHI is stored and the system is not a medical device (NFR-007) -- so HIPAA/HITECH, HL7/FHIR/DICOM interoperability, and FDA SaMD/EU MDR medical-device rules are treated as not applicable here. The GDPR-style baseline (NFR-006, NFR-009) and audit logging (US-023) are the closest implemented equivalents to the domain skill's 'minimum-necessary access,' 'audit of who viewed/changed a record,' and 'patient consent' topics, applied to employee (not patient) data.

**Related:** US-022, US-023, US-024, NFR-005, NFR-006, NFR-007, NFR-009, NFR-010

- ⚠ Human confirmation needed that the system truly never stores PHI, given the Healthcare industry tag -- this assumption underpins the decision to skip HIPAA-specific controls.
- ⚠ No WCAG accessibility requirement is specified anywhere in requirements despite the Healthcare industry context; confirm whether accessibility compliance is required for any patient- or clinician-facing use.
<!-- sdlc:auto:end narrative -->

<!-- sdlc:auto:start summary -->
**Requirements version:** v1  
**Delivery scope:** lightweight  
**Approved:** 2026-10-24

**Capabilities in scope:** Employee clock in/out from any personal device, Unpaid break start/stop within a shift, Worked duration computed and rolled up per day and per week, Regular vs overtime hours split at default thresholds (8h/day, 40h/week), Overnight shifts attributed to the day the shift starts, Per-employee timezone for correct local timestamps, Personal daily/weekly hours view, Employee sign-in to their own account

**Approved technology stack:**

| Layer | Choice | Rationale |
|---|---|---|
| backend | FastAPI | The core of this product is server-side logic — computing worked duration, rolling up daily/weekly regular vs overtime hours against configurable thresholds, handling timezones and overnight shifts, enforcing role-based access, and the correction-approval audit trail. FastAPI is a clean, well-structured Python API framework that handles all of this comfortably at your low concurrency, and makes the date/time and CSV work straightforward. |
| cloud | AWS | You need standard-availability hosting with encryption in transit and at rest and a GDPR-style privacy baseline for staff in mixed regions. AWS offers region choice, managed PostgreSQL, and straightforward encryption/backup controls, and can host this small internal tool cheaply while leaving room to formalise data-residency and retention as the org grows. |
| database | PostgreSQL | Attendance is relational, time-sensitive data: employees, teams, shifts, break intervals, correction requests, and an audit log all link together and must stay consistent. PostgreSQL enforces those relationships, handles timezone-aware timestamps natively (essential for your per-employee timezone and overnight-shift rules), and runs the date arithmetic behind your daily/weekly and overtime rollups reliably. |
| frontend | React | Your product is a single responsive web app used in-house by under ~50 staff clocking in, managers reviewing records, and HR exporting timesheets. It has no public pages that need to rank on search engines or load instantly for anonymous visitors, so a plain React single-page app covers every screen (clock-in, hours view, correction workflow, admin settings) on both phones and desktops without extra machinery. |
<!-- sdlc:auto:end summary -->

<!-- sdlc:auto:start epics -->
## EPIC-001: Authentication & Role-Based Access

Admin-provisioned accounts with email + password sign-in, password reset by email, and role-based access control across Employee, Manager and HR/Admin roles. No self-signup. Assumption: authentication is email + password only; mixed-region privacy baseline means access is strictly limited by role (employees see only their own data, managers only their team, HR/Admin org-wide).

### US-001: Employee sign-in to own account

**Priority:** critical

> As a employee, I want to sign in to the web app with my email and password from any device, so that I can access my own attendance and clock in/out.

| ID | Given | When | Then |
|---|---|---|---|
| AC-001 | I have an admin-provisioned account | I enter my correct email and password | I am signed in and taken to my personal dashboard showing my clock-in/out controls and my hours |
| AC-002 | I am on the sign-in page | I enter an incorrect email or password | I am refused access and shown a generic 'invalid credentials' message without revealing which field was wrong |
| AC-003 | I do not have an account | I look for a way to register | no self-signup option is available because accounts are admin-provisioned only |

### US-002: Password reset by email

**Priority:** high

> As a user, I want to reset my password via an emailed link, so that I can regain access if I forget my password without contacting an admin.

| ID | Given | When | Then |
|---|---|---|---|
| AC-004 | I am on the sign-in page and have forgotten my password | I request a reset for my registered email | a time-limited reset link is emailed to that address and I am shown a neutral confirmation regardless of whether the email exists |
| AC-005 | I have a valid, unexpired reset link | I set a new password meeting the password policy | my password is updated and I can sign in with it, and the link can no longer be reused |

### US-003: Role-based access enforcement

**Priority:** critical

> As a HR/Admin, I want each user's access to be limited to what their role permits, so that personal attendance data is only seen on a need-to-know basis per the privacy baseline.

| ID | Given | When | Then |
|---|---|---|---|
| AC-006 | I am signed in as an employee | I attempt to view another employee's records or any admin/manager screen | access is denied and only my own data and controls are available |
| AC-007 | I am signed in as a manager | I view attendance records | I can see only records for employees on my assigned team plus my own |
| AC-008 | I am signed in as HR/Admin | I view attendance records | I can see and edit records for all employees across the organisation |

## EPIC-002: Clock In/Out & Breaks

Employees (and managers/HR who also hold employee accounts) clock in and out from any personal device on the honour system, and start/stop unpaid breaks within an open shift. Timestamps are recorded in the employee's configured timezone; overnight shifts crossing midnight are supported. Assumption: honour-system from any device with no geofencing, kiosk or biometric method; accuracy relies on manager review and corrections.

### US-004: Clock in and out from a personal device

**Priority:** critical

> As a employee, I want to clock in when I start work and clock out when I finish from my own device, so that my worked time is recorded accurately.

| ID | Given | When | Then |
|---|---|---|---|
| AC-009 | I am signed in and have no open shift | I tap Clock In | a clock-in timestamp is recorded in my timezone and my shift shows as open |
| AC-010 | I have an open shift | I tap Clock Out | a clock-out timestamp is recorded, the shift is closed, and my worked duration is calculated |
| AC-011 | I have an open shift | I view my clock controls | the Clock In action is unavailable so I cannot start a second overlapping shift |
| AC-012 | my shift started before midnight and I clock out after midnight | the shift is closed | the whole shift is attributed to the day it started for rollup purposes |

### US-005: Start and stop unpaid breaks within a shift

**Priority:** high

> As a employee, I want to start and stop unpaid breaks during an open shift, so that break time is excluded from my paid worked duration.

| ID | Given | When | Then |
|---|---|---|---|
| AC-013 | I have an open shift and no break in progress | I tap Start Break | a break start timestamp is recorded and my shift shows a break in progress |
| AC-014 | I have a break in progress | I tap Stop Break | a break end timestamp is recorded and break time is subtracted from my worked duration |
| AC-015 | I have a break in progress | I attempt to clock out | I am prompted to end the break first or the break is auto-ended at clock-out, and the break is not counted as worked time |

### US-006: Record timestamps in the employee's timezone

**Priority:** high

> As a employee working in my own region, I want my clock events recorded and shown in my configured timezone, so that my daily/weekly hours reflect my local working day.

| ID | Given | When | Then |
|---|---|---|---|
| AC-016 | my account has a configured timezone | I clock in or out | the event timestamp is stored and displayed in that timezone and day boundaries use that timezone for rollups |

## EPIC-003: Worked Hours Computation & Overtime

The system computes worked duration per shift (excluding unpaid breaks) and rolls it up per day and per week, splitting regular vs overtime against admin-configurable thresholds defaulting to 8h/day and 40h/week. Assumption: thresholds are org-wide and admin-configurable; overnight shifts counted on their start day.

### US-007: Compute daily and weekly worked totals

**Priority:** critical

> As a employee, I want the system to total my worked hours per day and per week, so that I can see accurate totals without manual calculation.

| ID | Given | When | Then |
|---|---|---|---|
| AC-017 | I have one or more closed shifts on a day | the daily total is computed | it equals the sum of worked durations (clock-out minus clock-in minus unpaid breaks) for shifts attributed to that day |
| AC-018 | I have closed shifts across a week | the weekly total is computed | it equals the sum of the daily worked totals for that week |

### US-008: Split regular vs overtime hours

**Priority:** high

> As a HR/Admin, I want hours split into regular and overtime against configurable thresholds, so that payroll can be prepared correctly from exported timesheets.

| ID | Given | When | Then |
|---|---|---|---|
| AC-019 | the daily threshold is 8h and an employee works 10h in a day | the day is rolled up | 8h are shown as regular and 2h as overtime |
| AC-020 | the weekly threshold is 40h and cumulative weekly hours exceed 40h | the week is rolled up | hours beyond 40h are classified as overtime in the weekly total |
| AC-021 | an HR/Admin has changed the daily or weekly threshold from the defaults of 8h/40h | rollups are recomputed | the regular/overtime split uses the configured thresholds org-wide |

## EPIC-004: Personal Hours View

Employees can view their own daily and weekly hours, including regular, overtime and break time, and their current shift status.

### US-009: View my daily and weekly hours

**Priority:** high

> As a employee, I want to view my own daily and weekly hours and break time, so that I can confirm my attendance is recorded correctly.

| ID | Given | When | Then |
|---|---|---|---|
| AC-022 | I am signed in | I open my hours view | I see my worked hours per day and per week with regular, overtime and break time broken out, in my timezone |
| AC-023 | I have an open shift | I view my dashboard | I see my current shift status (clocked in, on break, or clocked out) and elapsed time so far |
| AC-024 | I am an employee | I use the hours view | I can only see my own hours and not any other employee's |

## EPIC-005: Manager Team Oversight & Missing/Late Flagging

Managers view their team's attendance records and hours and see entries flagged as missing or late against each employee's simple expected start time / standard daily hours. No full rostering. Managers also hold an employee account and can clock in themselves.

### US-010: View team records and hours

**Priority:** high

> As a manager, I want to view attendance records and rolled-up hours for my team, so that I can monitor attendance and prepare for payroll review.

| ID | Given | When | Then |
|---|---|---|---|
| AC-025 | I manage a team of employees | I open the team view | I see each team member's clock events and daily/weekly hours (regular, overtime, break) for a selected period |
| AC-026 | I am a manager | I view records | I see only employees assigned to my team and not other teams' data |

### US-011: See flagged missing or late entries

**Priority:** high

> As a manager, I want missing or late entries flagged against expected start time and daily hours, so that I can follow up and request or make corrections.

| ID | Given | When | Then |
|---|---|---|---|
| AC-027 | an employee has an expected start time and has not clocked in by that time | I view my team dashboard | that employee is flagged as missing/late for the day |
| AC-028 | an employee's worked hours for a day fall below their standard daily hours | the day is evaluated | the day is flagged as under expected hours for my review |

### US-012: Manager clocks in for themselves

**Priority:** medium

> As a manager, I want to clock in and out using my own employee account, so that my own attendance is tracked like any employee's.

| ID | Given | When | Then |
|---|---|---|---|
| AC-029 | I am a manager with an employee account | I use the clock controls | my clock-in/out and breaks are recorded and rolled up the same way as any employee |

## EPIC-006: Correction Request Workflow

Employees request corrections to their records (e.g. forgot to clock out); the relevant manager approves or rejects them; approvals update the record. All correction actions are captured in the audit trail and trigger email notifications.

### US-013: Submit a correction request

**Priority:** high

> As a employee, I want to request a correction to my clock records, so that mistakes like a forgotten clock-out can be fixed.

| ID | Given | When | Then |
|---|---|---|---|
| AC-030 | I have a record that is wrong or missing an entry | I submit a correction request with the proposed times and a reason | the request is saved as pending and my manager is notified by email |
| AC-031 | I have submitted a correction request | I view my requests | I can see its status (pending, approved, or rejected) |

### US-014: Approve or reject a correction request

**Priority:** high

> As a manager, I want to review and approve or reject my team's correction requests, so that records stay accurate while staying under my control.

| ID | Given | When | Then |
|---|---|---|---|
| AC-032 | a pending correction request exists for my team | I approve it | the affected record is updated with the corrected times, totals are recomputed, the employee is emailed, and the action is written to the audit log |
| AC-033 | a pending correction request exists for my team | I reject it with a reason | the record is unchanged, the employee is emailed with the reason, and the action is written to the audit log |

## EPIC-007: Email Notifications

Transactional email notifications for correction request submitted (to manager), correction approved/rejected (to employee), and optional reminders for missing clock-outs. Assumption: requires a transactional email provider credential (API key/SMTP); missing-clock-out reminders are optional/configurable.

### US-015: Notify on correction workflow events

**Priority:** medium

> As a user involved in a correction, I want to receive an email when a correction is submitted, approved or rejected, so that I act promptly without having to poll the app.

| ID | Given | When | Then |
|---|---|---|---|
| AC-034 | an employee submits a correction request | the request is saved | the responsible manager receives an email with the request details |
| AC-035 | a manager approves or rejects a request | the decision is recorded | the employee receives an email stating the outcome (and the reason if rejected) |
| AC-036 | the transactional email provider credential is not configured | a notification is triggered | the in-app action still completes and the notification failure is logged rather than blocking the workflow |

### US-016: Optional missing clock-out reminder

**Priority:** low

> As a employee, I want an optional reminder email if I appear to have forgotten to clock out, so that I can submit a correction sooner.

| ID | Given | When | Then |
|---|---|---|---|
| AC-037 | missing-clock-out reminders are enabled by an admin and my shift remains open beyond a reasonable window | the reminder check runs | I receive a reminder email prompting me to clock out or request a correction |
| AC-038 | missing-clock-out reminders are disabled | a shift remains open | no reminder email is sent |

## EPIC-008: HR/Admin Employee & Settings Management

HR/Admin add and remove employees, assign roles and teams, set per-employee timezone, expected start time and standard daily hours, edit any attendance record, and configure org-wide settings including overtime thresholds. Assumption: accounts are admin-provisioned (no self-signup).

### US-017: Add and remove employees

**Priority:** critical

> As a HR/Admin, I want to create and deactivate employee accounts with basic identity data, so that only current staff can access and be tracked in the system.

| ID | Given | When | Then |
|---|---|---|---|
| AC-039 | I am HR/Admin | I create an employee with name, email, role and team | an admin-provisioned account is created and the employee can set a password via an emailed invite/reset link |
| AC-040 | an employee leaves | I remove or deactivate their account | they can no longer sign in while their historical records remain for reporting unless deleted via a privacy request |

### US-018: Configure per-employee schedule and timezone

**Priority:** high

> As a HR/Admin, I want to set each employee's timezone, expected start time and standard daily hours, so that timestamps are local and missing/late flagging works without full rostering.

| ID | Given | When | Then |
|---|---|---|---|
| AC-041 | I am editing an employee | I set their timezone, expected start time and standard daily hours | these values are used for their rollups and missing/late flags |

### US-019: Edit any attendance record

**Priority:** high

> As a HR/Admin, I want to edit any employee's attendance record, so that I can fix data org-wide where a correction request is not the right path.

| ID | Given | When | Then |
|---|---|---|---|
| AC-042 | I am HR/Admin viewing a record | I edit the clock or break times | totals are recomputed and the change is captured in the audit log showing who changed what and when |

### US-020: Configure org-wide overtime thresholds

**Priority:** medium

> As a HR/Admin, I want to configure the daily and weekly overtime thresholds, so that the regular/overtime split matches our policy.

| ID | Given | When | Then |
|---|---|---|---|
| AC-043 | I open settings | I view the overtime thresholds | they default to 8h/day and 40h/week |
| AC-044 | I change the daily or weekly threshold and save | rollups and exports are generated | they apply the new thresholds org-wide |

## EPIC-009: CSV Timesheet Export

HR/Admin export timesheets to CSV for a selectable pay period, including per-employee regular hours, overtime hours, break time and daily/weekly totals, for manual payroll use. Assumption: no direct payroll integration; CSV is consumed manually.

### US-021: Export pay-period timesheet to CSV

**Priority:** high

> As a HR/Admin, I want to export a CSV timesheet for a selected pay period, so that payroll can be processed manually in our external system.

| ID | Given | When | Then |
|---|---|---|---|
| AC-045 | I am HR/Admin | I select a pay-period date range and export | a CSV is generated with per-employee regular hours, overtime hours, break time, and daily and weekly totals for that period |
| AC-046 | the export spans overnight shifts | the CSV is produced | each overnight shift is counted on the day it started, consistent with the in-app rollups |
| AC-047 | I am a manager or employee | I look for org-wide export | the org-wide export is unavailable to me and restricted to HR/Admin |

## EPIC-010: Privacy, Audit & Security

GDPR-style privacy baseline for mixed regions: role-limited access, employee notice/consent, and the ability to access, export and delete an employee's personal data. An audit log records edits, corrections and approvals. Encryption in transit and at rest; standard (non-clinical-grade) availability. Assumptions: stores only attendance + basic identity data, no PHI, not a medical device; no payments/billing.

### US-022: Access, export and delete personal data

**Priority:** medium

> As a HR/Admin handling a privacy request, I want to access, export and delete an employee's personal data, so that we can meet GDPR-style subject rights across mixed regions.

| ID | Given | When | Then |
|---|---|---|---|
| AC-048 | an employee makes a data-access request | I generate their personal-data export | a file is produced containing their identity and attendance data held in the system |
| AC-049 | an approved erasure request | I delete an employee's personal data | their personal data is removed or irreversibly anonymised and the deletion is recorded in the audit log |
| AC-050 | an employee's account is created | they first sign in | they are shown a privacy notice explaining what attendance and identity data is stored and why |

### US-023: Audit log of edits, corrections and approvals

**Priority:** high

> As a HR/Admin, I want an audit trail of record edits, corrections and approvals, so that we can see who changed what and when.

| ID | Given | When | Then |
|---|---|---|---|
| AC-051 | a record is edited, or a correction is submitted, approved or rejected | the action completes | an audit entry records the actor, the action, the affected record, before/after values where applicable, and the timestamp |
| AC-052 | I am HR/Admin | I view the audit log | I can review the recorded actions for the relevant employees |

### US-024: Encryption and standard availability

**Priority:** medium

> As a HR/Admin responsible for the system, I want personal data encrypted in transit and at rest with standard availability, so that employee data is protected without over-engineering for clinical-grade HA.

| ID | Given | When | Then |
|---|---|---|---|
| AC-053 | data is transmitted between browser and server | any request is made | it is served over encrypted transport (HTTPS/TLS) |
| AC-054 | personal and attendance data is stored | it is persisted | it is encrypted at rest |
| AC-055 | the system is an internal attendance tool | availability is considered | standard availability applies (no clinical-grade 24/7 HA) and no payment, billing or subscription functionality is included |
<!-- sdlc:auto:end epics -->
