"""Shared security primitives: password hashing, JWT issuance/verification,
and the `get_current_user` / `require_role` dependencies every router depends
on for authentication and role-based authorization.

`bearer_scheme` is kept with `auto_error=False` so routers not yet wired to
`get_current_user` (later sprints) keep working as before; `get_current_user`
itself fails closed on any missing or invalid token.
"""

from __future__ import annotations

import os
import time
import uuid
from dataclasses import dataclass

import jwt
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

bearer_scheme = HTTPBearer(auto_error=False)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRES_MINUTES = int(os.getenv("JWT_EXPIRES_MINUTES", "480"))

_UNAUTHENTICATED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated"
)


def hash_password(password: str) -> str:
    """Bcrypt-hash a plaintext password for storage."""
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """True when `password` matches the stored bcrypt hash."""
    try:
        return pwd_context.verify(password, password_hash)
    except ValueError:
        return False


@dataclass
class CurrentUser:
    """The signed-in identity, read straight from the verified JWT claims."""

    id: str
    email: str
    name: str
    role: str
    team: str | None
    timezone: str


def create_access_token(
    *,
    employee_id: uuid.UUID,
    email: str,
    name: str,
    role: str,
    team: uuid.UUID | None,
    timezone: str,
) -> str:
    """Issue a signed JWT carrying the identity, role and team a request needs."""
    now = int(time.time())
    payload = {
        "sub": str(employee_id),
        "email": email,
        "name": name,
        "role": role,
        "team": str(team) if team else None,
        "timezone": timezone,
        "iat": now,
        "exp": now + JWT_EXPIRES_MINUTES * 60,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Security(bearer_scheme),
) -> CurrentUser:
    """Verify the bearer JWT (signature, expiry) and return its claims.

    Fails closed: a missing header, a malformed token, a bad signature or an
    expired token all return the same 401 rather than leaking which part
    failed.
    """
    if credentials is None or not credentials.credentials:
        raise _UNAUTHENTICATED
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.PyJWTError:
        raise _UNAUTHENTICATED from None

    return CurrentUser(
        id=payload.get("sub", ""),
        email=payload.get("email", ""),
        name=payload.get("name", ""),
        role=payload.get("role", ""),
        team=payload.get("team"),
        timezone=payload.get("timezone", "UTC"),
    )


def require_role(*roles: str):
    """Dependency factory: 403s unless the signed-in user's role is listed.

    Built for reuse by later routers (employees, team, attendance) that need
    role-scoped authorization on top of `get_current_user`.
    """

    def _check(current_user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if current_user.role not in roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
        return current_user

    return _check
