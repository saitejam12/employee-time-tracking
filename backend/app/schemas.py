"""Pydantic request and response models.

One pair per entity in the approved data model, plus the placeholder every
generated route returns until it has been implemented, plus the real auth
schemas US-001 implements.
"""

from pydantic import BaseModel, Field


class StubResponse(BaseModel):
    """What a generated route returns until someone implements it.

    A stub that returns a typed body rather than raising keeps the service
    startable and its OpenAPI document complete, so the frontend can be built
    against the agreed shape while the handlers are still being written.
    """

    endpoint: str
    status: str = "not_implemented"
    detail: str = "Scaffolded from the approved API spec; no behaviour yet."


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    id: str
    name: str
    email: str
    role: str
    team: str | None = None
    timezone: str


class MeResponse(BaseModel):
    id: str
    name: str
    email: str
    role: str
    team: str | None = None
    timezone: str
    privacy_notice_acked: bool


class PasswordResetRequestIn(BaseModel):
    email: str


class PasswordResetConfirmIn(BaseModel):
    token: str
    new_password: str = Field(min_length=10)


class MessageResponse(BaseModel):
    message: str
