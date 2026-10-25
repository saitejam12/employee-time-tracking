"""SQLAlchemy models.

One class per entity in the approved data model (see
docs/sdlc/architecture/data-model.md and the `components.schemas` section of
docs/sdlc/architecture/api/openapi.yaml). `Base` is already bound to the
engine and `main.py` imports this module before it creates the schema.

Column types are picked to work against both the SQLite the scaffold defaults
to and the PostgreSQL 16 the architecture names: `Uuid` and `JSON` compile to
sensible equivalents on either backend, and the Postgres-only `citext`
extension type is left for a migration to add when something actually needs
case-insensitive email lookups enforced in the database rather than in a
query.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime, time
from decimal import Decimal

from sqlalchemy import (
    JSON,
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    Time,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    # References employees.id, which itself references teams.id -- `use_alter`
    # breaks that cycle so `Base.metadata.create_all` can order the tables.
    manager_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("employees.id", use_alter=True, name="fk_teams_manager_id"),
        nullable=True,
    )

    employees: Mapped[list[Employee]] = relationship(
        "Employee", back_populates="team", foreign_keys="Employee.team_id"
    )


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(320), nullable=False, unique=True)
    password_hash: Mapped[str | None] = mapped_column(Text, nullable=True)
    role: Mapped[str] = mapped_column(String(32), nullable=False)
    team_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    timezone: Mapped[str] = mapped_column(String(64), nullable=False)
    expected_start_time: Mapped[time | None] = mapped_column(Time, nullable=True)
    standard_daily_hours: Mapped[Decimal | None] = mapped_column(Numeric(5, 2), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    privacy_notice_acked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    team: Mapped[Team | None] = relationship(
        "Team", back_populates="employees", foreign_keys=[team_id]
    )
    shifts: Mapped[list[Shift]] = relationship("Shift", back_populates="employee")
    daily_rollups: Mapped[list[DailyRollup]] = relationship(
        "DailyRollup", back_populates="employee"
    )
    correction_requests: Mapped[list[CorrectionRequest]] = relationship(
        "CorrectionRequest",
        back_populates="employee",
        foreign_keys="CorrectionRequest.employee_id",
    )
    password_reset_tokens: Mapped[list[PasswordResetToken]] = relationship(
        "PasswordResetToken", back_populates="employee"
    )
    audit_entries: Mapped[list[AuditLogEntry]] = relationship(
        "AuditLogEntry", back_populates="actor"
    )


class Shift(Base):
    __tablename__ = "shifts"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    employee_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("employees.id"), nullable=False)
    clock_in_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    clock_out_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    work_date: Mapped[date] = mapped_column(Date, nullable=False)
    worked_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False)

    employee: Mapped[Employee] = relationship("Employee", back_populates="shifts")
    breaks: Mapped[list[Break]] = relationship("Break", back_populates="shift")
    correction_requests: Mapped[list[CorrectionRequest]] = relationship(
        "CorrectionRequest", back_populates="shift", foreign_keys="CorrectionRequest.shift_id"
    )


class Break(Base):
    __tablename__ = "breaks"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    shift_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("shifts.id"), nullable=False)
    break_start_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    break_end_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    shift: Mapped[Shift] = relationship("Shift", back_populates="breaks")


class DailyRollup(Base):
    __tablename__ = "daily_rollups"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    employee_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("employees.id"), nullable=False)
    work_date: Mapped[date] = mapped_column(Date, nullable=False)
    regular_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    overtime_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    break_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_missing_late: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_under_hours: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    employee: Mapped[Employee] = relationship("Employee", back_populates="daily_rollups")


class CorrectionRequest(Base):
    __tablename__ = "correction_requests"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    employee_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("employees.id"), nullable=False)
    shift_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("shifts.id"), nullable=True)
    proposed_clock_in_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    proposed_clock_out_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    reason: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="pending")
    reviewed_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("employees.id"), nullable=True)
    decision_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    employee: Mapped[Employee] = relationship(
        "Employee", back_populates="correction_requests", foreign_keys=[employee_id]
    )
    shift: Mapped[Shift | None] = relationship(
        "Shift", back_populates="correction_requests", foreign_keys=[shift_id]
    )
    reviewer: Mapped[Employee | None] = relationship("Employee", foreign_keys=[reviewed_by])


class OrgSettings(Base):
    __tablename__ = "org_settings"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    daily_threshold_hours: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    weekly_threshold_hours: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    missing_clockout_reminder_enabled: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    reminder_window_hours: Mapped[Decimal | None] = mapped_column(Numeric(5, 2), nullable=True)


class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    employee_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("employees.id"), nullable=False)
    token_hash: Mapped[str] = mapped_column(Text, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    used_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    employee: Mapped[Employee] = relationship("Employee", back_populates="password_reset_tokens")


class AuditLogEntry(Base):
    __tablename__ = "audit_log"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    actor_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("employees.id"), nullable=True)
    action: Mapped[str] = mapped_column(String(64), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(64), nullable=False)
    entity_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, nullable=True)
    before_value: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    after_value: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    actor: Mapped[Employee | None] = relationship("Employee", back_populates="audit_entries")


__all__ = [
    "Base",
    "Team",
    "Employee",
    "Shift",
    "Break",
    "DailyRollup",
    "CorrectionRequest",
    "OrgSettings",
    "PasswordResetToken",
    "AuditLogEntry",
]
