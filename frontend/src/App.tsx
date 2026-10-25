import { NavLink, Navigate, Outlet, Route, Routes } from "react-router-dom";

import SignIn from "@/screens/SignIn";
import ResetPassword from "@/screens/ResetPassword";
import MyTime from "@/screens/MyTime";
import Team from "@/screens/Team";
import Employees from "@/screens/Employees";
import Records from "@/screens/Records";
import Settings from "@/screens/Settings";
import { AuthProvider, ProtectedRoute, useAuth } from "@/lib/auth";

const navLinkClass = ({ isActive }: { isActive: boolean }) =>
  [
    "block rounded-[var(--brand-radius)] px-3 py-2 text-sm font-medium transition-colors",
    isActive ? "bg-[var(--brand-hover)] text-[var(--brand-fg)]" : "text-[var(--brand-fg-muted)]",
  ].join(" ");

// The screens behind sign-in render inside the side menu. Login and the other
// screens shown before sign-in render on their own, with no menu around them.
function Shell() {
  const { user } = useAuth();
  return (
    <div className="flex min-h-screen">
      <aside
        className="flex w-56 shrink-0 flex-col border-r p-4"
        style={{
          backgroundColor: "var(--brand-surface)",
          borderColor: "var(--brand-border)",
        }}
      >
        <p
          className="mb-4 px-3 text-sm font-semibold"
          style={{ fontFamily: "var(--brand-font-heading)" }}
        >
          {"Small employee time-tracking web app"}
        </p>
        <nav className="flex flex-col gap-1">
          <NavLink to="/my-time" className={navLinkClass}>
            {"My time"}
          </NavLink>
          <NavLink to="/team" className={navLinkClass}>
            {"My team"}
          </NavLink>
          <NavLink to="/employees" className={navLinkClass}>
            {"Employees"}
          </NavLink>
          <NavLink to="/records" className={navLinkClass}>
            {"Attendance records"}
          </NavLink>
          <NavLink to="/settings" className={navLinkClass}>
            {"Settings & audit log"}
          </NavLink>
        </nav>
        {user ? (
          <div
            className="mt-auto px-3 pt-4 text-xs"
            style={{ color: "var(--brand-fg-muted)" }}
          >
            {user.name} · {user.role}
          </div>
        ) : null}
      </aside>
      <main className="flex-1 overflow-auto">
        <Outlet />
      </main>
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/reset-password" element={<ResetPassword />} />
        <Route element={<ProtectedRoute />}>
          <Route element={<Shell />}>
            <Route path="/my-time" element={<MyTime />} />
            <Route path="/team" element={<Team />} />
            <Route path="/employees" element={<Employees />} />
            <Route path="/records" element={<Records />} />
            <Route path="/settings" element={<Settings />} />
          </Route>
        </Route>
        <Route path="*" element={<Navigate to="/sign-in" replace />} />
      </Routes>
    </AuthProvider>
  );
}
