<!-- sdlc:auto:start adr -->
# ADR-0003: Use PostgreSQL 16 for Database

Status: Proposed  
Date: 2026-10-24

## Context and Problem Statement

Which Database technology does the project use? Decided in architecture v1.

## Considered Options

- PostgreSQL 16
- MySQL
- SQLite

## Decision Outcome

Chosen option: PostgreSQL 16, because Attendance is relational and time-sensitive; PostgreSQL enforces the employee/team/shift/break/correction/audit relationships, stores timezone-aware timestamptz natively and runs the date arithmetic behind rollups reliably.

## Consequences

Needs a managed instance (RDS) rather than an embedded file DB, justified by consistency and timezone correctness.
<!-- sdlc:auto:end adr -->