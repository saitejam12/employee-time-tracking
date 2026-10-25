"""Shared security-scheme declaration.

Every endpoint the approved API spec marks `auth: JWT` depends on this scheme
so FastAPI's generated OpenAPI document carries the `bearerAuth` security
requirement the architecture specifies, and so every router has one place to
import a real JWT dependency from once it exists.

It does not verify anything yet: issuing and verifying the token is US-001
and role/team enforcement is US-003, both sprint work. Until then
`auto_error=False` means a request reaches the (still stubbed) handler
whether or not a bearer token is present, so this file does not block the
sprint that replaces it.
"""

from fastapi.security import HTTPBearer

bearer_scheme = HTTPBearer(auto_error=False)
