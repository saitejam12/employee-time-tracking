# Data Model

<!-- sdlc:auto:start entities -->
### teams

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| name | text | False | — | False |
| manager_id | uuid | False | employees.id | True |

### employees

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| name | text | False | — | False |
| email | citext | False | — | False |
| password_hash | text | False | — | True |
| role | text | False | — | False |
| team_id | uuid | False | teams.id | True |
| timezone | text | False | — | False |
| expected_start_time | time | False | — | True |
| standard_daily_hours | numeric | False | — | True |
| is_active | boolean | False | — | False |
| privacy_notice_acked_at | timestamptz | False | — | True |
| created_at | timestamptz | False | — | False |

### shifts

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| employee_id | uuid | False | employees.id | False |
| clock_in_at | timestamptz | False | — | False |
| clock_out_at | timestamptz | False | — | True |
| work_date | date | False | — | False |
| worked_minutes | integer | False | — | True |
| status | text | False | — | False |

### breaks

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| shift_id | uuid | False | shifts.id | False |
| break_start_at | timestamptz | False | — | False |
| break_end_at | timestamptz | False | — | True |

### daily_rollups

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| employee_id | uuid | False | employees.id | False |
| work_date | date | False | — | False |
| regular_minutes | integer | False | — | False |
| overtime_minutes | integer | False | — | False |
| break_minutes | integer | False | — | False |
| is_missing_late | boolean | False | — | False |
| is_under_hours | boolean | False | — | False |

### correction_requests

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| employee_id | uuid | False | employees.id | False |
| shift_id | uuid | False | shifts.id | True |
| proposed_clock_in_at | timestamptz | False | — | True |
| proposed_clock_out_at | timestamptz | False | — | True |
| reason | text | False | — | False |
| status | text | False | — | False |
| reviewed_by | uuid | False | employees.id | True |
| decision_reason | text | False | — | True |
| reviewed_at | timestamptz | False | — | True |
| created_at | timestamptz | False | — | False |

### org_settings

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| daily_threshold_hours | numeric | False | — | False |
| weekly_threshold_hours | numeric | False | — | False |
| missing_clockout_reminder_enabled | boolean | False | — | False |
| reminder_window_hours | numeric | False | — | True |

### password_reset_tokens

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| employee_id | uuid | False | employees.id | False |
| token_hash | text | False | — | False |
| expires_at | timestamptz | False | — | False |
| used_at | timestamptz | False | — | True |

### audit_log

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| actor_id | uuid | False | employees.id | True |
| action | text | False | — | False |
| entity_type | text | False | — | False |
| entity_id | uuid | False | — | True |
| before_value | jsonb | False | — | True |
| after_value | jsonb | False | — | True |
| created_at | timestamptz | False | — | False |
<!-- sdlc:auto:end entities -->

<!-- sdlc:auto:start relationships -->
| Source | Target | Type |
|---|---|---|
| teams | employees | one-to-many |
| employees | shifts | one-to-many |
| shifts | breaks | one-to-many |
| employees | daily_rollups | one-to-many |
| employees | correction_requests | one-to-many |
| shifts | correction_requests | one-to-many |
| employees | password_reset_tokens | one-to-many |
| employees | audit_log | one-to-many |
<!-- sdlc:auto:end relationships -->

<!-- sdlc:auto:start er-diagram -->
```mermaid
erDiagram
  teams {
    uuid id PK
    text name
    uuid manager_id FK
  }
  employees {
    uuid id PK
    text name
    citext email
    text password_hash
    text role
    uuid team_id FK
    text timezone
    time expected_start_time
    numeric standard_daily_hours
    boolean is_active
    timestamptz privacy_notice_acked_at
    timestamptz created_at
  }
  shifts {
    uuid id PK
    uuid employee_id FK
    timestamptz clock_in_at
    timestamptz clock_out_at
    date work_date
    integer worked_minutes
    text status
  }
  breaks {
    uuid id PK
    uuid shift_id FK
    timestamptz break_start_at
    timestamptz break_end_at
  }
  daily_rollups {
    uuid id PK
    uuid employee_id FK
    date work_date
    integer regular_minutes
    integer overtime_minutes
    integer break_minutes
    boolean is_missing_late
    boolean is_under_hours
  }
  correction_requests {
    uuid id PK
    uuid employee_id FK
    uuid shift_id FK
    timestamptz proposed_clock_in_at
    timestamptz proposed_clock_out_at
    text reason
    text status
    uuid reviewed_by FK
    text decision_reason
    timestamptz reviewed_at
    timestamptz created_at
  }
  org_settings {
    uuid id PK
    numeric daily_threshold_hours
    numeric weekly_threshold_hours
    boolean missing_clockout_reminder_enabled
    numeric reminder_window_hours
  }
  password_reset_tokens {
    uuid id PK
    uuid employee_id FK
    text token_hash
    timestamptz expires_at
    timestamptz used_at
  }
  audit_log {
    uuid id PK
    uuid actor_id FK
    text action
    text entity_type
    uuid entity_id
    jsonb before_value
    jsonb after_value
    timestamptz created_at
  }
  teams ||--o{ employees : "one-to-many"
  employees ||--o{ shifts : "one-to-many"
  shifts ||--o{ breaks : "one-to-many"
  employees ||--o{ daily_rollups : "one-to-many"
  employees ||--o{ correction_requests : "one-to-many"
  shifts ||--o{ correction_requests : "one-to-many"
  employees ||--o{ password_reset_tokens : "one-to-many"
  employees ||--o{ audit_log : "one-to-many"
```
<!-- sdlc:auto:end er-diagram -->
