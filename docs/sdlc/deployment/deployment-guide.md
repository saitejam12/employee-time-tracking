# Deployment Guide

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start how-it-deploys -->
Pushes to `main` run `.github/workflows/deploy.yml`, which builds the API image (if there is a backend) and deploys the SPA to AWS Amplify. Commits touching only `docs/sdlc/**` don't deploy. Deployments can also be started from the platform's Deployment tab.
<!-- sdlc:auto:end how-it-deploys -->

<!-- sdlc:auto:start environments -->
| Name | Service | Runtime | Scaling | Environment |
|---|---|---|---|---|
| frontend_static | React SPA on S3 + CloudFront | Static build (CDN) | CDN-served, no instance scaling | dev |
| api_service | FastAPI on ECS Fargate | Python 3.12 container (uvicorn) | 1 task (low concurrency, <50 users) | dev |
| worker_service | arq worker on ECS Fargate | Python 3.12 container | 1 task | dev |
| postgres_db | Amazon RDS for PostgreSQL 16 | Managed PostgreSQL 16 | Single instance, encryption at rest (KMS), automated backups | dev |
| redis_queue | Redis 7 (container / ElastiCache) | redis:7-alpine | Single node | dev |
| sendgrid | SendGrid transactional email | SaaS API | Managed by provider | dev |
<!-- sdlc:auto:end environments -->

<!-- sdlc:auto:start live -->
_Not deployed yet._
<!-- sdlc:auto:end live -->

<!-- sdlc:auto:start topology -->
```mermaid
graph LR
  n_frontend_static["frontend_static<br/>React SPA on S3 + CloudFront"]
  n_api_service["api_service<br/>FastAPI on ECS Fargate"]
  n_worker_service["worker_service<br/>arq worker on ECS Fargate"]
  n_postgres_db["postgres_db<br/>Amazon RDS for PostgreSQL 16"]
  n_redis_queue["redis_queue<br/>Redis 7 (container / ElastiCache)"]
  n_sendgrid["sendgrid<br/>SendGrid transactional email"]
  n_frontend_static -->|"HTTPS"| n_api_service
  n_api_service -->|"TLS (PostgreSQL)"| n_postgres_db
  n_api_service -->|"TCP (Redis)"| n_redis_queue
  n_worker_service -->|"TCP (Redis)"| n_redis_queue
  n_worker_service -->|"TLS (PostgreSQL)"| n_postgres_db
  n_worker_service -->|"HTTPS"| n_sendgrid
```
<!-- sdlc:auto:end topology -->
