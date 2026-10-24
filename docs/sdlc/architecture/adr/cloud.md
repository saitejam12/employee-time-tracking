<!-- sdlc:auto:start adr -->
# ADR-0004: Use AWS for Cloud

Status: Proposed  
Date: 2026-10-24

## Context and Problem Statement

Which Cloud technology does the project use? Decided in architecture v1.

## Considered Options

- AWS
- Azure
- GCP

## Decision Outcome

Chosen option: AWS, because Provides region choice for the mixed-region GDPR-style baseline, managed PostgreSQL (RDS) with encryption at rest and backups, and cheap hosting for a small internal tool.

## Consequences

Standard availability only (single region/instance) by design; data-residency and retention can be formalised later as the org grows.
<!-- sdlc:auto:end adr -->