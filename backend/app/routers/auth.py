"""`POST/GET /auth/...` -- sign-in, session profile, password reset, privacy ack.

Login issues a JWT carrying id/role/team; `/me` reads the signed-in identity
back from that token. Password-reset request/confirm never reveal whether an
email exists or which part of a reset attempt failed (NFR-003), and reset
tokens are random, stored hashed, time-limited and single-use (AC-005).
"""

from __future__ import annotations

import hashlib
import os
import secrets
import uuid
from datetime import UTC, datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Security, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Employee, PasswordResetToken
from app.schemas import (
    LoginRequest,
    LoginResponse,
    MeResponse,
    MessageResponse,
    PasswordResetConfirmIn,
    PasswordResetRequestIn,
    StubResponse,
)
from app.security import (
    CurrentUser,
    bearer_scheme,
    create_access_token,
    get_current_user,
    hash_password,
    verify_password,
)
from app.services import send_password_reset_email

router = APIRouter(prefix="/auth", tags=["auth"])

RESET_TOKEN_TTL_MINUTES = int(os.getenv("PASSWORD_RESET_TTL_MINUTES", "60"))

_INVALID_CREDENTIALS_DETAIL = "Invalid credentials"
_INVALID_RESET_TOKEN_DETAIL = "Invalid or expired token"


def _hash_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def _password_meets_policy(password: str) -> bool:
    if len(password) < 10:
        return False
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_letter and has_digit


def _find_employee_by_email(db: Session, email: str) -> Employee | None:
    return db.execute(
        select(Employee).where(func.lower(Employee.email) == email.strip().lower())
    ).scalar_one_or_none()


@router.post("/login", response_model=LoginResponse)
async def login(payload: LoginRequest, db: Session = Depends(get_db)) -> LoginResponse:
    """Sign in with email and password; returns JWT or generic error."""
    employee = _find_employee_by_email(db, payload.email)

    if (
        employee is None
        or not employee.is_active
        or not employee.password_hash
        or not verify_password(payload.password, employee.password_hash)
    ):
        # Unknown email, wrong password and deactivated account all collapse
        # into the same response so a caller cannot tell them apart.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=_INVALID_CREDENTIALS_DETAIL
        )

    token = create_access_token(
        employee_id=employee.id,
        email=employee.email,
        name=employee.name,
        role=employee.role,
        team=employee.team_id,
        timezone=employee.timezone,
    )
    return LoginResponse(
        access_token=token,
        id=str(employee.id),
        name=employee.name,
        email=employee.email,
        role=employee.role,
        team=str(employee.team_id) if employee.team_id else None,
        timezone=employee.timezone,
    )


@router.get("/me", response_model=MeResponse)
async def read_me(
    current_user: CurrentUser = Depends(get_current_user), db: Session = Depends(get_db)
) -> MeResponse:
    """Current user profile, role, timezone and privacy-notice state."""
    try:
        employee_id = uuid.UUID(current_user.id)
    except (ValueError, AttributeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated"
        ) from None

    employee = db.get(Employee, employee_id)
    if employee is None or not employee.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    return MeResponse(
        id=str(employee.id),
        name=employee.name,
        email=employee.email,
        role=employee.role,
        team=str(employee.team_id) if employee.team_id else None,
        timezone=employee.timezone,
        privacy_notice_acked=employee.privacy_notice_acked_at is not None,
    )


@router.post("/password-reset/request", response_model=MessageResponse)
async def password_reset_request(
    payload: PasswordResetRequestIn, db: Session = Depends(get_db)
) -> MessageResponse:
    """Request a reset link; always returns neutral confirmation, sends email
    only when the account exists and is active."""
    employee = _find_employee_by_email(db, payload.email)

    if employee is not None and employee.is_active:
        raw_token = secrets.token_urlsafe(32)
        reset_token = PasswordResetToken(
            employee_id=employee.id,
            token_hash=_hash_token(raw_token),
            expires_at=datetime.now(UTC) + timedelta(minutes=RESET_TOKEN_TTL_MINUTES),
        )
        db.add(reset_token)
        db.commit()

        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
        reset_link = f"{frontend_url}/reset-password?token={raw_token}"
        send_password_reset_email(employee.email, reset_link)

    return MessageResponse(
        message="If an account exists for that email, a reset link has been sent."
    )


@router.post("/password-reset/confirm", response_model=MessageResponse)
async def password_reset_confirm(
    payload: PasswordResetConfirmIn, db: Session = Depends(get_db)
) -> MessageResponse:
    """Set a new password using a single-use time-limited token."""
    if not _password_meets_policy(payload.new_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 10 characters and include a letter and a digit.",
        )

    token_hash = _hash_token(payload.token)
    reset_token = db.execute(
        select(PasswordResetToken).where(PasswordResetToken.token_hash == token_hash)
    ).scalar_one_or_none()

    now = datetime.now(UTC)
    if reset_token is None or reset_token.used_at is not None or reset_token.expires_at < now:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=_INVALID_RESET_TOKEN_DETAIL
        )

    employee = db.get(Employee, reset_token.employee_id)
    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=_INVALID_RESET_TOKEN_DETAIL
        )

    employee.password_hash = hash_password(payload.new_password)
    reset_token.used_at = now
    db.commit()

    return MessageResponse(message="Password updated. You can now sign in.")


@router.post(
    "/privacy-notice/ack",
    response_model=StubResponse,
    dependencies=[Security(bearer_scheme)],
)
async def acknowledge_privacy_notice() -> StubResponse:
    """Record acknowledgement of the privacy notice at first sign-in."""
    return StubResponse(endpoint="POST /auth/privacy-notice/ack")
