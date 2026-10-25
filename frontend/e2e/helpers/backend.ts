// Test-only bridge into the backend process the Playwright webServer boots
// (see ../../playwright.config.ts). There is no admin-signup UI to create a
// fixture account through (there is deliberately no sign-up at all -- see
// AC-003), so these helpers write/read the same SQLite file the live backend
// uses, via a short python subprocess run from backend/'s own virtualenv.
//
// `captureResetToken` patches `sendgrid.SendGridAPIClient.send` for the one
// subprocess call that generates a token, so the suite never calls SendGrid
// for real and still gets the raw token the real request handler minted.
//
// Risk: this assumes `python3` on PATH resolves to the same interpreter/venv
// the webServer's `pip install -r requirements.txt` populated, and that
// DATABASE_URL is the backend's SQLite default (no Postgres override) in this
// environment. See the QA report for this ticket.
import { execFileSync } from "node:child_process";
import path from "node:path";

const BACKEND_DIR = path.resolve(__dirname, "..", "..", "..", "backend");

function runPython(script: string, args: string[]): Record<string, unknown> {
  const output = execFileSync("python3", ["-c", script, ...args], {
    cwd: BACKEND_DIR,
    encoding: "utf-8",
  });
  const lastLine = output.trim().split("\n").filter(Boolean).pop();
  if (!lastLine) {
    throw new Error(`backend helper produced no output for script, args=${JSON.stringify(args)}`);
  }
  return JSON.parse(lastLine);
}

const SEED_SCRIPT = `
import sys, json, uuid
from passlib.context import CryptContext
from app.database import SessionLocal, Base, engine
from app import models

Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

email, password, role, is_active = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] == "true"
db = SessionLocal()
existing = db.query(models.Employee).filter_by(email=email).first()
if existing:
    db.delete(existing)
    db.commit()
emp = models.Employee(
    id=uuid.uuid4(),
    name="E2E Test User",
    email=email,
    password_hash=pwd_context.hash(password),
    role=role,
    timezone="Europe/London",
    is_active=is_active,
)
db.add(emp)
db.commit()
db.close()
print(json.dumps({"ok": True}))
`;

export function seedEmployee(
  email: string,
  password: string,
  role: "employee" | "manager" | "hr_admin" = "employee",
  isActive = true,
): void {
  const result = runPython(SEED_SCRIPT, [email, password, role, String(isActive)]);
  if (!result.ok) {
    throw new Error(`seedEmployee failed: ${JSON.stringify(result)}`);
  }
}

const CAPTURE_RESET_TOKEN_SCRIPT = `
import sys, json, re
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app

email = sys.argv[1]

def fake_response():
    r = MagicMock()
    r.status_code = 202
    return r

with patch("sendgrid.SendGridAPIClient.send", return_value=fake_response()) as mock_send:
    client = TestClient(app)
    resp = client.post("/auth/password-reset/request", json={"email": email})
    if mock_send.call_args is None:
        print(json.dumps({"ok": False, "error": "no email dispatched", "status": resp.status_code}))
    else:
        args, kwargs = mock_send.call_args
        message = args[0] if args else kwargs.get("message")
        payload = message.get() if hasattr(message, "get") else message
        text = payload if isinstance(payload, str) else json.dumps(payload, default=str)
        match = re.search(r"token=([A-Za-z0-9\\-_.]+)", text)
        if not match:
            print(json.dumps({"ok": False, "error": "token not found in email", "status": resp.status_code}))
        else:
            print(json.dumps({"ok": True, "token": match.group(1), "status": resp.status_code}))
`;

export function captureResetToken(email: string): { ok: boolean; token?: string; error?: string } {
  const result = runPython(CAPTURE_RESET_TOKEN_SCRIPT, [email]);
  return result as { ok: boolean; token?: string; error?: string };
}
