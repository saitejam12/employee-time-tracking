<!-- sdlc:auto:start adr -->
# ADR-0001: Use React 19 for Frontend

Status: Proposed  
Date: 2026-10-24

## Context and Problem Statement

Which Frontend technology does the project use? Decided in architecture v1.

## Considered Options

- React 19
- Next.js
- Vue

## Decision Outcome

Chosen option: React 19, because An in-house responsive SPA covers every screen (clock controls, hours view, team oversight, corrections, admin) for under ~50 staff with no public/SEO pages, served statically via CloudFront.

## Consequences

No SSR, so first load relies on client bundle; acceptable for an authenticated internal tool.
<!-- sdlc:auto:end adr -->