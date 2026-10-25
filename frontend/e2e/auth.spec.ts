import { expect, test } from "@playwright/test";

import { seedEmployee } from "./helpers/backend";

// AC-001: correct credentials land on the personal dashboard with clock controls and hours.
test("signing in with correct credentials lands on the personal dashboard", async ({ page }) => {
  const email = `qa-signin-${Date.now()}@example.com`;
  const password = "CorrectHorse9!";
  seedEmployee(email, password, "employee");

  await page.goto("/sign-in");
  await page.getByLabel(/work email/i).fill(email);
  await page.getByLabel(/^password$/i).fill(password);
  await page.getByRole("button", { name: /^sign in$/i }).click();

  await expect(page).toHaveURL(/\/my-time/);
  await expect(page.getByRole("button", { name: /clock in/i })).toBeVisible();
  await expect(page.locator('[aria-label="Hours summary"]')).toBeVisible();
});

// AC-002, AC-003: generic failure message, no field hint, no sign-up affordance.
test("wrong credentials show a generic message with no field hint and no sign-up link", async ({
  page,
}) => {
  await page.goto("/sign-in");
  await page.getByLabel(/work email/i).fill("nobody@example.com");
  await page.getByLabel(/^password$/i).fill("WhateverPassword1");
  await page.getByRole("button", { name: /^sign in$/i }).click();

  const alert = page.getByRole("alert");
  await expect(alert).toContainText(/credentials were refused/i);

  // Never guard on which field was wrong -- the generic banner is the whole point.
  await expect(page.getByText(/no account found|incorrect password|email not found/i)).toHaveCount(
    0,
  );

  // There is no sign-up anywhere on the page (AC-003).
  await expect(
    page.getByRole("link", { name: /sign up|register|create an account/i }),
  ).toHaveCount(0);
  await expect(
    page.getByRole("button", { name: /sign up|register|create an account/i }),
  ).toHaveCount(0);
});

// NFR-013: the sign-in journey must work at a phone-sized viewport too.
test.describe("mobile viewport", () => {
  test.use({ viewport: { width: 375, height: 812 } });

  test("signing in with correct credentials works at 375x812", async ({ page }) => {
    const email = `qa-signin-mobile-${Date.now()}@example.com`;
    const password = "CorrectHorse9!";
    seedEmployee(email, password, "employee");

    await page.goto("/sign-in");
    await page.getByLabel(/work email/i).fill(email);
    await page.getByLabel(/^password$/i).fill(password);
    await page.getByRole("button", { name: /^sign in$/i }).click();

    await expect(page).toHaveURL(/\/my-time/);
    await expect(page.getByRole("button", { name: /clock in/i })).toBeVisible();
  });
});
