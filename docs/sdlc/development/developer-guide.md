# Developer Guide

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start status -->
_Up to date._
<!-- sdlc:auto:end status -->

<!-- sdlc:auto:start source -->
Generated from commit `59df5bc` · model `claude-sonnet-5`
<!-- sdlc:auto:end source -->

<!-- sdlc:auto:start overview -->
This repository contains two generated, loosely-coupled applications for a small employee time-tracking tool: a React 19 single-page frontend (Vite-built, currently rendering seeded sample data rather than live API calls) and a FastAPI 0.115 backend that currently exposes only a health-check endpoint, since no backend architecture had been approved when it was generated. The backend defaults to a local SQLite database so it runs without any external services, while docker-compose.yml provisions Postgres and Redis for when the real architecture is implemented.
<!-- sdlc:auto:end overview -->

<!-- sdlc:auto:start prerequisites -->
- Node.js (for Vite 6 / React 19 / TypeScript 5.6 toolchain)
- npm
- Python 3.12
- pip
- Docker and Docker Compose (optional, for Postgres/Redis services)
<!-- sdlc:auto:end prerequisites -->

<!-- sdlc:auto:start setup -->
1. Clone the repository
2. cd frontend && npm install
3. cd backend && pip install -r requirements.txt
4. (optional) copy .env.example to .env and adjust values such as DATABASE_URL/ALLOWED_ORIGINS
5. (optional) docker-compose up -d to start Postgres and Redis if targeting the full architecture instead of the SQLite default
<!-- sdlc:auto:end setup -->

<!-- sdlc:auto:start run -->
| Name | Command | Description |
|---|---|---|
| frontend dev | `cd frontend && npm run dev` | Starts the Vite dev server for the React SPA (seeded sample data, no live backend wiring yet) |
| frontend build | `cd frontend && npm run build` | Bundles the app with Vite; does not typecheck |
| frontend preview | `cd frontend && npm run preview` | Serves the production build locally |
| backend dev | `cd backend && uvicorn app.main:app --reload` | Runs the FastAPI app with auto-reload; creates SQLite tables on startup and serves /health |
| compose up | `docker-compose up -d` | Starts Postgres 16 and Redis 7 containers defined in docker-compose.yml |
<!-- sdlc:auto:end run -->

<!-- sdlc:auto:start structure -->
| Path | Purpose |
|---|---|
| `frontend/` | React + Vite SPA; approved screens rendering seeded sample data |
| `frontend/src` | App source: main.tsx entry, lib/ (api client, ui, icons, navigate), index.css |
| `frontend/e2e` | Playwright end-to-end specs |
| `backend/` | FastAPI service scaffold |
| `backend/app` | Application code: main.py entrypoint, database.py (SQLAlchemy engine/session), models.py, schemas.py, services.py, routers/ |
| `backend/tests` | Pytest tests (currently health check only) |
| `.quorq/` | Platform handoff metadata (handoff.json) |
| `docker-compose.yml` | Local Postgres and Redis services for the approved architecture |
| `.env.example` | Example environment variables for local configuration |
<!-- sdlc:auto:end structure -->

<!-- sdlc:auto:start conventions -->
- Backend: one router per architecture component owning endpoints, one route per spec'd endpoint (backend/app/routers/)
- Unimplemented backend routes return a typed StubResponse rather than raising, keeping the service startable and OpenAPI complete
- Backend models live in models.py (SQLAlchemy, inheriting database.Base); request/response shapes live in schemas.py (Pydantic)
- Backend defaults to SQLite (DATABASE_URL env var overrides it, e.g. for Postgres) so it runs without a database server
- Backend tables are created via Base.metadata.create_all on startup; no migrations yet
- CORS origins are controlled via ALLOWED_ORIGINS env var (comma-separated), defaulting to the Vite dev server origins
- Frontend API access is centralized in src/lib/api.ts (apiFetch helper, VITE_API_BASE_URL / VITE_API_SECRET_KEY env vars), though screens do not call it yet
- Frontend component tests sit beside the components they cover and run under Vitest with jsdom
- Frontend uses ESLint + Prettier for linting/formatting; backend uses ruff for both
<!-- sdlc:auto:end conventions -->

<!-- sdlc:auto:start testing -->
| Name | Command | Description |
|---|---|---|
| backend tests | `cd backend && pytest` | Runs pytest suite (tests/test_health.py) |
| backend lint | `cd backend && ruff check .` | Lints backend Python code |
| backend format check | `cd backend && ruff format .` | Formats backend Python code |
| frontend unit tests | `cd frontend && npm test` | Runs Vitest component tests |
| frontend lint | `cd frontend && npm run lint` | Runs ESLint across the frontend app |
| frontend format | `cd frontend && npm run format` | Formats frontend files with Prettier |
| frontend typecheck | `cd frontend && npm run typecheck` | Runs tsc --noEmit (not enforced by build) |
| frontend e2e install | `cd frontend && npm run test:e2e:install` | Installs the Chromium browser needed for Playwright |
| frontend e2e | `cd frontend && npm run test:e2e` | Runs Playwright acceptance tests; builds/serves the app (and boots the backend) locally unless E2E_BASE_URL is set |
<!-- sdlc:auto:end testing -->

<!-- sdlc:auto:start troubleshooting -->
| Problem | Solution |
|---|---|
| Frontend build succeeds but tsc reports type errors | npm run build does not typecheck; run npm run typecheck separately with cd frontend to catch issues like untyped useState before deploying |
| Backend API calls from the frontend fail due to CORS | Set ALLOWED_ORIGINS on the backend to the frontend's actual origin (comma-separated for multiple), or rely on the default dev origins (localhost:5173) when running npm run dev |
| Backend data doesn't persist as expected or you need a real database | Set the DATABASE_URL env var (default is sqlite:///./app.db); use docker-compose up to start the Postgres 16 service for a real database |
| pytest fails with 'cannot import app' when run outside backend/ | Run pytest from the backend/ directory so pytest.ini's pythonpath = . applies |
| Playwright e2e tests fail to start | Run npm run test:e2e:install first to fetch the Chromium browser; without E2E_BASE_URL set, Playwright will install backend deps and boot both the backend (uvicorn) and the built frontend itself |
<!-- sdlc:auto:end troubleshooting -->
