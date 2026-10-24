<!-- sdlc:auto:start adr -->
# ADR-0002: Use FastAPI 0.115 for Backend

Status: Proposed  
Date: 2026-10-24

## Context and Problem Statement

Which Backend technology does the project use? Decided in architecture v1.

## Considered Options

- FastAPI 0.115
- Django REST Framework
- Flask

## Decision Outcome

Chosen option: FastAPI 0.115, because The product is server-side date/time logic: worked-duration and daily/weekly rollups, regular/overtime split, overnight attribution, timezone handling, RBAC and the correction audit trail — all straightforward in FastAPI at low concurrency, with easy CSV output.

## Consequences

Fewer batteries-included admin tools than Django, so admin screens are built in the React SPA.
<!-- sdlc:auto:end adr -->