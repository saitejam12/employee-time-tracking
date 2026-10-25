import * as React from "react";
import { Navigate, Outlet } from "react-router-dom";

import {
  type AuthUser,
  clearToken,
  getMe,
  getToken,
  login as apiLogin,
  setToken as storeToken,
} from "@/lib/api";

interface AuthState {
  token: string | null;
  user: AuthUser | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = React.createContext<AuthState | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [token, setToken] = React.useState<string | null>(() => getToken());
  const [user, setUser] = React.useState<AuthUser | null>(null);
  const [loading, setLoading] = React.useState<boolean>(() => !!getToken());

  React.useEffect(() => {
    let cancelled = false;
    if (!token) {
      setLoading(false);
      setUser(null);
      return undefined;
    }
    setLoading(true);
    getMe()
      .then((me) => {
        if (!cancelled) setUser(me);
      })
      .catch(() => {
        if (!cancelled) {
          clearToken();
          setToken(null);
        }
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [token]);

  const login = React.useCallback(async (email: string, password: string) => {
    const { access_token, user: loggedInUser } = await apiLogin(email, password);
    storeToken(access_token);
    setToken(access_token);
    setUser(loggedInUser);
  }, []);

  const logout = React.useCallback(() => {
    clearToken();
    setToken(null);
    setUser(null);
  }, []);

  const value = React.useMemo(
    () => ({ token, user, loading, login, logout }),
    [token, user, loading, login, logout],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthState {
  const ctx = React.useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within an AuthProvider");
  return ctx;
}

/** Guards the routes behind sign-in: no token, no entry -- straight back to /sign-in. */
export function ProtectedRoute() {
  const { token, loading } = useAuth();
  if (loading) return null;
  if (!token) return <Navigate to="/sign-in" replace />;
  return <Outlet />;
}
