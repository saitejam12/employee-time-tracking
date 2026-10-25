// @ts-nocheck -- matches the loose JS the approved sibling screens were authored under.
// Route: /reset-password?token=... -- reached from the link emailed by
// POST /auth/password-reset/request. Enforces the password policy client-side,
// then posts to POST /auth/password-reset/confirm. An expired or already-used
// token renders the API's own error message -- there is no client-side simulation.
import React from "react";
import { useNavigate, useSearchParams } from "react-router-dom";

import * as UI from "@/lib/ui";
import { Icons } from "@/lib/icons";
import { brand } from "@/lib/brand";
import { apiErrorMessage, confirmPasswordReset } from "@/lib/api";

const { Button, Input, Label } = UI;
const { Check, X, AlertCircle } = Icons;

const MONO = "'Martian Mono', 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace";
const SANS = "'Public Sans', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif";
const INK_RED = "#9a2b17";

export default function Screen() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const token = searchParams.get("token") ?? "";

  const c = {
    primary: brand.primaryColor,
    ink: brand.neutralColor,
    bg: brand.backgroundColor,
    surface: "rgba(255,255,255,0.80)",
    line: "rgba(31,36,32,0.16)",
    lineStrong: "rgba(31,36,32,0.34)",
    muted: "rgba(31,36,32,0.66)",
    faint: "rgba(31,36,32,0.45)",
    radius: brand.radius || "0rem",
  };

  const [pw1, setPw1] = React.useState("");
  const [pw2, setPw2] = React.useState("");
  const [busy, setBusy] = React.useState(false);
  const [formError, setFormError] = React.useState(null);

  const pwChecks = [
    { k: "len", label: "At least 10 characters", ok: pw1.length >= 10 },
    { k: "num", label: "Contains a number", ok: /\d/.test(pw1) },
    { k: "alpha", label: "Contains a letter", ok: /[a-zA-Z]/.test(pw1) },
    { k: "match", label: "Both entries match", ok: pw1.length > 0 && pw1 === pw2 },
  ];
  const pwValid = pwChecks.every((x) => x.ok);

  const inputStyle = {
    fontFamily: SANS,
    fontSize: "15px",
    color: c.ink,
    backgroundColor: "rgba(255,255,255,0.92)",
    border: `1px solid ${c.lineStrong}`,
    borderRadius: c.radius,
    height: "44px",
    width: "100%",
    padding: "0 12px",
  };

  const primaryBtnStyle = (disabled) => ({
    backgroundColor: c.primary,
    color: "rgba(255,255,255,0.97)",
    borderRadius: c.radius,
    border: `1px solid ${c.primary}`,
    fontFamily: MONO,
    fontSize: "12px",
    letterSpacing: "0.1em",
    textTransform: "uppercase",
    height: "48px",
    width: "100%",
    opacity: disabled ? 0.45 : 1,
    cursor: disabled ? "not-allowed" : "pointer",
  });

  const label = (htmlFor, text) => (
    <Label
      htmlFor={htmlFor}
      className="block text-[11px] font-semibold uppercase tracking-[0.14em]"
      style={{ fontFamily: MONO, color: c.muted, marginBottom: "6px", letterSpacing: "0.12em" }}
    >
      {text}
    </Label>
  );

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!pwValid || !token) return;
    setFormError(null);
    setBusy(true);
    try {
      await confirmPasswordReset(token, pw1);
      navigate("/sign-in");
    } catch (err) {
      setFormError(
        apiErrorMessage(
          err,
          "That reset link no longer works. Ask an admin to send you a new one.",
        ),
      );
    } finally {
      setBusy(false);
    }
  };

  return (
    <main
      className="flex min-h-screen w-full items-center justify-center px-5 py-10 sm:px-10"
      style={{ backgroundColor: c.bg, color: c.ink, fontFamily: SANS }}
    >
      <div
        className="w-full max-w-[460px] p-8 sm:p-10"
        style={{
          backgroundColor: c.surface,
          border: `1px solid ${c.lineStrong}`,
          borderRadius: c.radius,
        }}
      >
        <h1
          className="text-[30px] leading-[1.12] font-semibold"
          style={{ fontFamily: MONO, color: c.ink, letterSpacing: "-0.02em" }}
        >
          Choose a new password
        </h1>
        <p
          className="mt-3 max-w-[48ch] text-[14.5px] leading-relaxed"
          style={{ color: c.muted, fontFamily: SANS }}
        >
          Setting it here signs you out of other devices and burns the link.
        </p>

        {!token ? (
          <div
            className="mt-7 flex gap-3 p-4"
            role="alert"
            style={{
              border: `1px solid ${INK_RED}`,
              borderLeftWidth: "4px",
              backgroundColor: "rgba(154,43,23,0.06)",
              borderRadius: c.radius,
            }}
          >
            <AlertCircle
              className="h-4 w-4 shrink-0"
              style={{ color: INK_RED, marginTop: "2px" }}
              aria-hidden="true"
            />
            <p className="text-[13.5px] leading-relaxed" style={{ color: c.ink }}>
              This link is missing its token. Use the link from your reset email.
            </p>
          </div>
        ) : null}

        {formError ? (
          <div
            className="mt-7 flex gap-3 p-4"
            role="alert"
            style={{
              border: `1px solid ${INK_RED}`,
              borderLeftWidth: "4px",
              backgroundColor: "rgba(154,43,23,0.06)",
              borderRadius: c.radius,
            }}
          >
            <AlertCircle
              className="h-4 w-4 shrink-0"
              style={{ color: INK_RED, marginTop: "2px" }}
              aria-hidden="true"
            />
            <p className="text-[13.5px] leading-relaxed" style={{ color: c.ink }}>
              {formError}
            </p>
          </div>
        ) : null}

        <form onSubmit={handleSubmit} noValidate className="mt-7">
          <div className="mb-5">
            {label("new-password", "New password")}
            <Input
              id="new-password"
              name="new_password"
              type="password"
              autoComplete="new-password"
              value={pw1}
              onChange={(e) => setPw1(e.target.value)}
              aria-describedby="pw-policy"
              style={inputStyle}
            />
          </div>
          <div className="mb-5">
            {label("confirm-password", "Type it again")}
            <Input
              id="confirm-password"
              name="confirm_password"
              type="password"
              autoComplete="new-password"
              value={pw2}
              onChange={(e) => setPw2(e.target.value)}
              style={inputStyle}
            />
          </div>

          <ul id="pw-policy" className="mb-6 space-y-1.5">
            {pwChecks.map((chk) => (
              <li
                key={chk.k}
                className="flex items-center gap-2 text-[13px]"
                style={{ fontFamily: SANS }}
              >
                {chk.ok ? (
                  <Check
                    className="h-3.5 w-3.5 shrink-0"
                    style={{ color: c.primary }}
                    aria-hidden="true"
                  />
                ) : (
                  <X
                    className="h-3.5 w-3.5 shrink-0"
                    style={{ color: c.faint }}
                    aria-hidden="true"
                  />
                )}
                <span style={{ color: chk.ok ? c.ink : c.muted }}>
                  {chk.label}
                  <span className="sr-only">{chk.ok ? " -- met" : " -- not met yet"}</span>
                </span>
              </li>
            ))}
          </ul>

          <Button
            type="submit"
            disabled={!pwValid || !token || busy}
            aria-busy={busy ? "true" : "false"}
            style={primaryBtnStyle(!pwValid || !token || busy)}
          >
            {busy ? "Updating…" : "Set password and sign in"}
          </Button>
        </form>
      </div>
    </main>
  );
}
