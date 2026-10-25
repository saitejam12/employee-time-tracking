// @ts-nocheck -- matches the loose JS the approved design was authored under; see lib/ui's
// Input (no forwardRef) for why a plain TSX pass would otherwise reject the `ref` prop here.
// Wired to the real auth API (POST /auth/login, POST /auth/password-reset/request).
// Visual direction preserved from the approved "Punch Card" design; identity now comes
// entirely from the API -- there is no seeded account list or demo credential anymore.
import React from "react";

import * as UI from "@/lib/ui";
import { Icons } from "@/lib/icons";
import { brand } from "@/lib/brand";
import { useNavigate } from "@/lib/navigate";
import { useAuth } from "@/lib/auth";
import { apiErrorMessage, requestPasswordReset } from "@/lib/api";

const { Button, Input, Label, Separator } = UI;
const { Check, X, ChevronRight, Users, Bell, Clock, ArrowLeft, AlertCircle } = Icons;

const MONO = "'Martian Mono', 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace";
const SANS = "'Public Sans', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif";

// Red stamp ink -- the one semantic colour outside the brand roles, used only for refusals.
const INK_RED = "#9a2b17";

const SPECIMEN_ROWS = [
  { day: "MON 19 OCT", in: "08:57", out: "17:34", brk: "0:42", net: "7:55", flag: null },
  { day: "TUE 20 OCT", in: "09:04", out: "18:10", brk: "0:35", net: "8:31", flag: "OT 0:31" },
  { day: "WED 21 OCT", in: "—", out: "—", brk: "—", net: "0:00", flag: "MISSING" },
  { day: "THU 22 OCT", in: "08:49", out: "16:02", brk: "0:30", net: "6:43", flag: "UNDER" },
  { day: "FRI 23 OCT", in: "22:12", out: "06:28", brk: "0:45", net: "7:31", flag: "OVERNIGHT" },
];

const FIELD_LABEL_CLASS = "block text-[11px] font-semibold uppercase tracking-[0.14em]";

export default function Screen() {
  const navigate = useNavigate();
  const auth = useAuth();

  const c = {
    primary: brand.primaryColor,
    accent: brand.accentColor,
    ink: brand.neutralColor,
    bg: brand.backgroundColor,
    surface: "rgba(255,255,255,0.80)",
    sunk: "rgba(255,255,255,0.55)",
    line: "rgba(31,36,32,0.16)",
    lineStrong: "rgba(31,36,32,0.34)",
    muted: "rgba(31,36,32,0.66)",
    faint: "rgba(31,36,32,0.45)",
    onDark: "rgba(255,255,255,0.92)",
    onDarkMuted: "rgba(255,255,255,0.60)",
    lineDark: "rgba(255,255,255,0.16)",
    radius: brand.radius || "0rem",
  };

  const [view, setView] = React.useState("signin"); // signin | forgot | sent
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [resetEmail, setResetEmail] = React.useState("");
  const [busy, setBusy] = React.useState(null); // 'signin' | 'reset' | null
  const [formError, setFormError] = React.useState(null); // { title, body }
  const [fieldErrors, setFieldErrors] = React.useState({});
  const [now, setNow] = React.useState(() => new Date());

  const timers = React.useRef([]);
  const firstFieldRef = React.useRef(null);

  React.useEffect(() => {
    const id = window.setInterval(() => setNow(new Date()), 1000);
    return () => window.clearInterval(id);
  }, []);

  React.useEffect(() => {
    return () => {
      timers.current.forEach((t) => window.clearTimeout(t));
      timers.current = [];
    };
  }, []);

  React.useEffect(() => {
    if (firstFieldRef.current) firstFieldRef.current.focus();
  }, [view]);

  const clockTz = "Europe/London";

  const fmtClock = (d, tz) =>
    new Intl.DateTimeFormat("en-GB", {
      timeZone: tz,
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: false,
    }).format(d);

  const fmtDate = (d, tz) =>
    new Intl.DateTimeFormat("en-GB", {
      timeZone: tz,
      weekday: "short",
      day: "2-digit",
      month: "short",
      year: "numeric",
    })
      .format(d)
      .toUpperCase();

  const handleSignIn = async (e) => {
    e.preventDefault();
    const errs = {};
    if (!email.trim()) errs.email = "Enter the email your account was issued to.";
    else if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.trim()))
      errs.email = "That does not look like an email address.";
    if (!password) errs.password = "Enter your password.";
    setFieldErrors(errs);
    if (Object.keys(errs).length) {
      setFormError(null);
      return;
    }
    setFormError(null);
    setBusy("signin");
    try {
      await auth.login(email.trim(), password);
      navigate("my-time");
    } catch {
      // Deliberately generic -- never says which of email/password was wrong, and
      // never reveals whether the account exists, is deactivated, or anything else.
      setFormError({
        title: "Those credentials were refused",
        body: "The email and password do not match an active account.",
      });
    } finally {
      setBusy(null);
    }
  };

  const handleResetRequest = async (e) => {
    e.preventDefault();
    const target = resetEmail.trim();
    if (!target || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(target)) {
      setFieldErrors({ resetEmail: "Enter the email address your account uses." });
      return;
    }
    setFieldErrors({});
    setFormError(null);
    setBusy("reset");
    try {
      await requestPasswordReset(target);
      setView("sent");
    } catch (err) {
      setFormError({
        title: "Could not send that",
        body: apiErrorMessage(err, "Something went wrong sending the reset email. Try again."),
      });
    } finally {
      setBusy(null);
    }
  };

  const onKeyDown = (e) => {
    if (e.key === "Escape" && (view === "forgot" || view === "sent")) {
      setView("signin");
      setFieldErrors({});
      setFormError(null);
    }
  };

  const css = `
    @keyframes pcIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
    @keyframes pcBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0.18; } }
    .pc-in { animation: pcIn 240ms cubic-bezier(.2,.8,.3,1) both; }
    .pc-blink { animation: pcBlink 1.1s steps(1, end) infinite; }
    .pc-f:focus-visible { outline: 2px solid ${c.primary}; outline-offset: 2px; }
    .pc-btn { transition: background-color 140ms linear, color 140ms linear, border-color 140ms linear, opacity 140ms linear; }
    .pc-input { transition: border-color 120ms linear, background-color 120ms linear; }
    @media (prefers-reduced-motion: reduce) {
      .pc-in, .pc-blink { animation: none !important; }
      .pc-btn, .pc-input { transition: none !important; }
    }
  `;

  const perfStrip = (holeColor) => ({
    backgroundImage: `radial-gradient(circle 4px at 12px 12px, ${holeColor} 98%, transparent 100%)`,
    backgroundSize: "24px 24px",
    backgroundRepeat: "repeat-y",
    backgroundPosition: "0 14px",
  });

  const inputStyle = (bad) => ({
    fontFamily: SANS,
    fontSize: "15px",
    color: c.ink,
    backgroundColor: bad ? "rgba(154,43,23,0.05)" : "rgba(255,255,255,0.92)",
    border: `1px solid ${bad ? INK_RED : c.lineStrong}`,
    borderRadius: c.radius,
    height: "44px",
    width: "100%",
    padding: "0 12px",
  });

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

  const ghostBtnStyle = {
    backgroundColor: "transparent",
    color: c.ink,
    borderRadius: c.radius,
    border: `1px solid ${c.lineStrong}`,
    fontFamily: MONO,
    fontSize: "11px",
    letterSpacing: "0.09em",
    textTransform: "uppercase",
    height: "44px",
    padding: "0 14px",
    cursor: "pointer",
  };

  const label = (htmlFor, text) => (
    <Label
      htmlFor={htmlFor}
      className={FIELD_LABEL_CLASS}
      style={{ fontFamily: MONO, color: c.muted, marginBottom: "6px", letterSpacing: "0.12em" }}
    >
      {text}
    </Label>
  );

  const fieldError = (id, msg) =>
    msg ? (
      <p
        id={id}
        className="mt-2 flex items-start gap-2 text-[13px] leading-snug"
        style={{ color: INK_RED, fontFamily: SANS }}
      >
        <X className="h-4 w-4 shrink-0" style={{ marginTop: "1px" }} aria-hidden="true" />
        <span>{msg}</span>
      </p>
    ) : null;

  const banner = () => {
    if (!formError) return null;
    return (
      <div
        className="pc-in mb-6 flex gap-3 p-4"
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
        <div>
          <p
            className="text-[12px] font-semibold uppercase tracking-[0.1em]"
            style={{ fontFamily: MONO, color: INK_RED }}
          >
            {formError.title}
          </p>
          <p
            className="mt-1.5 text-[13.5px] leading-relaxed"
            style={{ color: c.ink, fontFamily: SANS }}
          >
            {formError.body}
          </p>
        </div>
      </div>
    );
  };

  /* ---------------------------------------------------------------- panels */

  const signInPanel = (
    <div className="pc-in">
      <p
        className="mb-3 text-[11px] uppercase tracking-[0.22em]"
        style={{ fontFamily: MONO, color: c.faint }}
      >
        Card No. — / —
      </p>
      <h1
        className="text-[32px] leading-[1.1] font-semibold"
        style={{ fontFamily: MONO, color: c.ink, letterSpacing: "-0.02em" }}
      >
        Sign in
      </h1>
      <p
        className="mt-3 max-w-[46ch] text-[14.5px] leading-relaxed"
        style={{ color: c.muted, fontFamily: SANS }}
      >
        Signing in opens your card. Clocking in and out happens after, from the card itself.
      </p>

      <div className="mt-7">{banner()}</div>

      <form onSubmit={handleSignIn} noValidate>
        <div className="mb-5">
          {label("signin-email", "Work email")}
          <Input
            id="signin-email"
            name="email"
            type="email"
            autoComplete="username"
            className="pc-input pc-f"
            ref={firstFieldRef}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            aria-invalid={fieldErrors.email ? "true" : undefined}
            aria-describedby={fieldErrors.email ? "signin-email-err" : undefined}
            style={inputStyle(!!fieldErrors.email)}
          />
          {fieldError("signin-email-err", fieldErrors.email)}
        </div>

        <div className="mb-6">
          {label("signin-password", "Password")}
          <Input
            id="signin-password"
            name="password"
            type="password"
            autoComplete="current-password"
            className="pc-input pc-f"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            aria-invalid={fieldErrors.password ? "true" : undefined}
            aria-describedby={fieldErrors.password ? "signin-password-err" : undefined}
            style={inputStyle(!!fieldErrors.password)}
          />
          {fieldError("signin-password-err", fieldErrors.password)}
        </div>

        <Button
          type="submit"
          className="pc-btn pc-f inline-flex items-center justify-center gap-2.5"
          disabled={busy === "signin"}
          aria-busy={busy === "signin" ? "true" : "false"}
          style={primaryBtnStyle(busy === "signin")}
        >
          {busy === "signin" ? (
            <React.Fragment>
              <span
                className="pc-blink inline-block h-2.5 w-2.5"
                style={{ backgroundColor: c.accent }}
                aria-hidden="true"
              />
              Checking credentials…
            </React.Fragment>
          ) : (
            <React.Fragment>
              <Clock className="h-4 w-4" aria-hidden="true" />
              Sign in
            </React.Fragment>
          )}
        </Button>

        <div className="mt-4 flex justify-center">
          <button
            type="button"
            className="pc-f pc-btn text-[13px] underline underline-offset-4"
            style={{ color: c.primary, fontFamily: SANS, padding: "10px 8px", minHeight: "44px" }}
            onClick={() => {
              setResetEmail(email);
              setFieldErrors({});
              setFormError(null);
              setView("forgot");
            }}
          >
            Forgotten your password?
          </button>
        </div>
      </form>

      <div className="my-7" style={{ color: c.line }}>
        <Separator />
      </div>

      <div className="flex gap-3">
        <Users
          className="h-4 w-4 shrink-0"
          style={{ color: c.faint, marginTop: "2px" }}
          aria-hidden="true"
        />
        <p className="text-[13px] leading-relaxed" style={{ color: c.muted, fontFamily: SANS }}>
          <span className="font-semibold" style={{ color: c.ink }}>
            There is no sign-up.
          </span>{" "}
          Accounts are admin-provisioned. If you are new, ask an admin to create yours -- you will
          get an invite link by email.
        </p>
      </div>
    </div>
  );

  const forgotPanel = (
    <div className="pc-in">
      <button
        type="button"
        className="pc-f pc-btn mb-6 inline-flex items-center gap-2 text-[11px] uppercase tracking-[0.12em]"
        style={{ fontFamily: MONO, color: c.muted, padding: "10px 2px", minHeight: "44px" }}
        onClick={() => {
          setView("signin");
          setFieldErrors({});
          setFormError(null);
        }}
      >
        <ArrowLeft className="h-4 w-4" aria-hidden="true" />
        Back to sign in
      </button>
      <h1
        className="text-[30px] leading-[1.12] font-semibold"
        style={{ fontFamily: MONO, color: c.ink, letterSpacing: "-0.02em" }}
      >
        Reset your password
      </h1>
      <p
        className="mt-3 max-w-[48ch] text-[14.5px] leading-relaxed"
        style={{ color: c.muted, fontFamily: SANS }}
      >
        We will email a link that works once and expires after a short window. Your attendance
        records are untouched by this.
      </p>

      <div className="mt-7">{banner()}</div>

      <form onSubmit={handleResetRequest} noValidate className="mt-2">
        <div className="mb-6">
          {label("reset-email", "Work email")}
          <Input
            id="reset-email"
            name="reset_email"
            type="email"
            autoComplete="username"
            className="pc-input pc-f"
            ref={firstFieldRef}
            value={resetEmail}
            onChange={(e) => setResetEmail(e.target.value)}
            aria-invalid={fieldErrors.resetEmail ? "true" : undefined}
            aria-describedby={fieldErrors.resetEmail ? "reset-email-err" : undefined}
            style={inputStyle(!!fieldErrors.resetEmail)}
          />
          {fieldError("reset-email-err", fieldErrors.resetEmail)}
        </div>
        <Button
          type="submit"
          className="pc-btn pc-f inline-flex items-center justify-center gap-2.5"
          disabled={busy === "reset"}
          aria-busy={busy === "reset" ? "true" : "false"}
          style={primaryBtnStyle(busy === "reset")}
        >
          {busy === "reset" ? (
            <React.Fragment>
              <span
                className="pc-blink inline-block h-2.5 w-2.5"
                style={{ backgroundColor: c.accent }}
                aria-hidden="true"
              />
              Sending…
            </React.Fragment>
          ) : (
            "Email me a reset link"
          )}
        </Button>
      </form>
    </div>
  );

  const sentPanel = (
    <div className="pc-in">
      <div
        className="mb-6 inline-flex h-11 w-11 items-center justify-center"
        style={{ border: `1px solid ${c.primary}`, color: c.primary, borderRadius: c.radius }}
      >
        <Check className="h-5 w-5" aria-hidden="true" />
      </div>
      <h1
        className="text-[30px] leading-[1.12] font-semibold"
        style={{ fontFamily: MONO, color: c.ink, letterSpacing: "-0.02em" }}
      >
        Check your inbox
      </h1>
      <p
        className="mt-4 max-w-[50ch] text-[14.5px] leading-relaxed"
        style={{ color: c.muted, fontFamily: SANS }}
      >
        If{" "}
        <span style={{ color: c.ink, fontFamily: MONO, fontSize: "13px" }}>
          {resetEmail.trim()}
        </span>{" "}
        belongs to an account here, a reset link is on its way. We do not confirm whether an
        address is registered.
      </p>

      <div
        className="mt-6 flex gap-3 p-4"
        style={{
          border: `1px dashed ${c.lineStrong}`,
          backgroundColor: c.sunk,
          borderRadius: c.radius,
        }}
      >
        <Bell
          className="h-4 w-4 shrink-0"
          style={{ color: c.faint, marginTop: "2px" }}
          aria-hidden="true"
        />
        <p className="text-[13px] leading-relaxed" style={{ color: c.muted, fontFamily: SANS }}>
          Nothing after a few minutes? Look in spam, then ask an admin to re-issue the link.
        </p>
      </div>

      <div className="mt-7 flex flex-wrap gap-3">
        <Button
          type="button"
          className="pc-btn pc-f inline-flex items-center justify-center gap-2"
          style={ghostBtnStyle}
          onClick={() => setView("signin")}
        >
          Back to sign in
          <ChevronRight className="h-4 w-4" aria-hidden="true" />
        </Button>
      </div>
    </div>
  );

  const panel = view === "signin" ? signInPanel : view === "forgot" ? forgotPanel : sentPanel;

  /* ------------------------------------------------------------- the page */

  return (
    <main
      className="min-h-screen w-full"
      style={{ backgroundColor: c.bg, color: c.ink, fontFamily: SANS }}
      onKeyDown={onKeyDown}
    >
      <style>{css}</style>

      <div className="grid min-h-screen grid-cols-1 lg:grid-cols-[1fr_minmax(480px,0.92fr)]">
        {/* ---- form column (first in DOM, right on desktop) ---- */}
        <section className="order-1 flex justify-center px-5 py-10 sm:px-10 lg:order-2 lg:items-center lg:py-16">
          <div className="w-full max-w-[460px]">
            <div
              className="relative"
              style={{
                backgroundColor: c.surface,
                border: `1px solid ${c.lineStrong}`,
                borderRadius: c.radius,
              }}
            >
              <div
                className="absolute inset-y-0 left-0 w-6"
                style={{ ...perfStrip(c.bg), borderRight: `1px solid ${c.line}` }}
                aria-hidden="true"
              />
              <div className="py-9 pl-12 pr-7 sm:pl-14 sm:pr-10">{panel}</div>
            </div>
          </div>
        </section>

        {/* ---- recorder column ---- */}
        <section
          className="order-2 flex flex-col justify-between px-6 py-10 sm:px-10 lg:order-1 lg:py-16"
          style={{ backgroundColor: c.ink, color: c.onDark }}
        >
          <div>
            <div className="flex items-center gap-3">
              <span
                className="inline-block h-6 w-6"
                style={{ backgroundColor: c.accent }}
                aria-hidden="true"
              />
              <span
                className="text-[15px] font-semibold uppercase"
                style={{ fontFamily: MONO, letterSpacing: "0.18em", color: c.onDark }}
              >
                Hourstamp
              </span>
            </div>
            <p
              className="mt-4 max-w-[40ch] text-[13.5px] leading-relaxed"
              style={{ color: c.onDarkMuted }}
            >
              The attendance recorder for your organisation.
            </p>

            <div
              className="mt-10"
              style={{ borderTop: `1px solid ${c.lineDark}`, paddingTop: "20px" }}
            >
              <p
                className="text-[10.5px] uppercase tracking-[0.2em]"
                style={{ fontFamily: MONO, color: c.onDarkMuted }}
              >
                Recorder clock · {clockTz}
              </p>
              <p
                className="mt-2 text-[46px] leading-none sm:text-[56px]"
                style={{
                  fontFamily: MONO,
                  fontVariantNumeric: "tabular-nums",
                  color: c.accent,
                  letterSpacing: "-0.03em",
                }}
              >
                {fmtClock(now, clockTz)}
              </p>
              <p
                className="mt-3 text-[11px] uppercase tracking-[0.2em]"
                style={{
                  fontFamily: MONO,
                  color: c.onDarkMuted,
                  fontVariantNumeric: "tabular-nums",
                }}
              >
                {fmtDate(now, clockTz)}
              </p>
            </div>
          </div>

          {/* specimen punch card */}
          <div className="mt-12">
            <div
              className="relative"
              style={{
                backgroundColor: "rgba(255,255,255,0.055)",
                border: `1px solid ${c.lineDark}`,
                borderRadius: c.radius,
              }}
            >
              <div
                className="absolute inset-y-0 left-0 w-6"
                style={{ ...perfStrip(c.ink), borderRight: `1px solid ${c.lineDark}` }}
                aria-hidden="true"
              />
              <div className="py-6 pl-11 pr-5 sm:pr-7">
                <div className="flex flex-wrap items-baseline justify-between gap-3">
                  <h2
                    className="text-[12px] uppercase"
                    style={{ fontFamily: MONO, letterSpacing: "0.16em", color: c.onDark }}
                  >
                    Specimen card · wk 43
                  </h2>
                  <span
                    className="px-2 py-0.5 text-[10px] uppercase tracking-[0.14em]"
                    style={{
                      fontFamily: MONO,
                      color: c.ink,
                      backgroundColor: c.accent,
                      borderRadius: c.radius,
                    }}
                  >
                    Not a live record
                  </span>
                </div>

                <table
                  className="mt-5 w-full text-left"
                  style={{
                    fontFamily: MONO,
                    fontVariantNumeric: "tabular-nums",
                    borderCollapse: "collapse",
                  }}
                >
                  <caption className="sr-only">
                    Specimen week of attendance showing clock-in, clock-out, break and net hours
                    per day
                  </caption>
                  <thead>
                    <tr style={{ borderBottom: `1px solid ${c.lineDark}` }}>
                      {["Day", "In", "Out", "Brk", "Net"].map((h) => (
                        <th
                          key={h}
                          scope="col"
                          className="pb-2 text-[9.5px] uppercase tracking-[0.14em] font-normal"
                          style={{
                            color: c.onDarkMuted,
                            textAlign: h === "Day" ? "left" : "right",
                          }}
                        >
                          {h}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {SPECIMEN_ROWS.map((r) => (
                      <tr
                        key={r.day}
                        style={{ borderBottom: `1px solid ${c.lineDark}`, height: "36px" }}
                      >
                        <th
                          scope="row"
                          className="text-[11px] font-normal"
                          style={{ color: c.onDark, textAlign: "left", whiteSpace: "nowrap" }}
                        >
                          {r.day}
                          {r.flag ? (
                            <span
                              className="ml-2 inline-block px-1.5 py-[1px] text-[9px] uppercase tracking-[0.1em]"
                              style={{
                                color: r.flag === "MISSING" ? c.ink : c.onDark,
                                backgroundColor: r.flag === "MISSING" ? c.accent : "transparent",
                                border: r.flag === "MISSING" ? "none" : `1px solid ${c.lineDark}`,
                              }}
                            >
                              {r.flag}
                            </span>
                          ) : null}
                        </th>
                        <td className="text-right text-[11.5px]" style={{ color: c.onDarkMuted }}>
                          {r.in}
                        </td>
                        <td className="text-right text-[11.5px]" style={{ color: c.onDarkMuted }}>
                          {r.out}
                        </td>
                        <td className="text-right text-[11.5px]" style={{ color: c.onDarkMuted }}>
                          {r.brk}
                        </td>
                        <td className="text-right text-[12px]" style={{ color: c.onDark }}>
                          {r.net}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                  <tfoot>
                    <tr style={{ height: "36px" }}>
                      <th
                        scope="row"
                        className="text-[10px] uppercase tracking-[0.14em] font-normal"
                        style={{ color: c.onDarkMuted, textAlign: "left" }}
                      >
                        Week · reg 30:09 / ot 0:31
                      </th>
                      <td
                        colSpan={4}
                        className="text-right text-[15px]"
                        style={{ color: c.accent }}
                      >
                        30:40
                      </td>
                    </tr>
                  </tfoot>
                </table>
              </div>
            </div>

            <p
              className="mt-6 max-w-[48ch] text-[12px] leading-relaxed"
              style={{ color: c.onDarkMuted }}
            >
              Served over TLS; cards are encrypted at rest. Nothing on a card is ever overwritten
              -- an approved correction prints beneath the original stamp.
            </p>
          </div>
        </section>
      </div>
    </main>
  );
}
