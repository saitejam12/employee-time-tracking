"""Shared fixtures for the auth / password-reset suites.

Each test gets its own in-memory SQLite database (via a `StaticPool` so the
single connection survives across the threadpool `TestClient` dispatches
through) wired in place of the app's real `get_db` dependency, so tests never
touch the `app.db` file a developer's own session is using.
"""

from __future__ import annotations

import uuid
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from passlib.context import CryptContext
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app import models
from app.database import Base, get_db
from app.main import app

# Matches the bcrypt pin called out in requirements.txt for US-001/US-002 password
# hashing -- see the comment there for why the pin exists.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@pytest.fixture()
def db_session() -> Iterator[Session]:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    testing_session_local = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    session = testing_session_local()
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


@pytest.fixture()
def client(db_session: Session) -> Iterator[TestClient]:
    def override_get_db() -> Iterator[Session]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_db, None)


@pytest.fixture()
def employee_factory(db_session: Session):
    """Create an employee directly in the DB, bypassing the (admin-only) API."""

    def _make(
        *,
        email: str,
        password: str = "CorrectHorse9!",
        role: str = "employee",
        is_active: bool = True,
        team_id: uuid.UUID | None = None,
        name: str = "Test Employee",
    ) -> models.Employee:
        employee = models.Employee(
            id=uuid.uuid4(),
            name=name,
            email=email,
            password_hash=pwd_context.hash(password),
            role=role,
            team_id=team_id,
            timezone="Europe/London",
            is_active=is_active,
        )
        db_session.add(employee)
        db_session.commit()
        db_session.refresh(employee)
        return employee

    return _make
