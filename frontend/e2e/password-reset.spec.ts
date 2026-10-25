import { expect, test } from "@playwright/test";

import { captureResetToken, seedEmployee } from "./helpers/backend";

// AC-004: neutral confirmation whether or not the email is registered.
test("requesting a reset shows the same neutral confirmation for a registered and an unregistered email", async ({
  page,
}) => {
  const registeredEmail = `qa-reset-${Date.now()}@example.com`;
  seedEmployee(registeredEmail, "OldPassword9!", "employee");

  await page.goto("/sign-in");
  await page.getByRole("button", { name: /forgotten your password/i }).click();
  await page.getByLabel(/work email/i).fill(registeredEmail);
  await page.getByRole("button", { name: /email me a reset link/i }).click();

  await expect(page.getByText(/check your inbox/i)).toBeVisible();
  await expect(
    page.getByText(/we do not confirm whether an address is registered/i),
  ).toBeVisible();

  await page.getByRole("button", { name: /back to sign in/i }).click();
  await page.getByRole("button", { name: /forgotten your password/i }).click();
  await page.getByLabel(/work email/i).fill(`qa-reset-unregistered-${Date.now()}@example.com`);
  await page.getByRole("button", { name: /email me a reset link/i }).click();

  await expect(page.getByText(/check your inbox/i)).toBeVisible();
  await expect(
    page.getByText(/we do not confirm whether an address is registered/i),
  ).toBeVisible();
});

// AC-004/AC-005: opening a reset link sets a new password that then signs in.
test("opening a valid reset link sets a new password that then signs in", async ({ page }) => {
  const email = `qa-reset-flow-${Date.now()}@example.com`;
  const newPassword = "BrandNewPass1";
  seedEmployee(email, "OldPassword9!", "employee");

  const captured = captureResetToken(email);
  expect(
    captured.ok,
    `could not capture a reset token from the dispatched email: ${captured.error ?? "unknown"}`,
  ).toBeTruthy();

  await page.goto(`/reset-password?token=${captured.token}`);
  await page.getByLabel(/new password/i).fill(newPassword);
  await page.getByLabel(/type it again/i).fill(newPassword);
  await page.getByRole("button", { name: /set password and sign in/i }).click();

  await expect(page).toHaveURL(/\/sign-in/);

  await page.getByLabel(/work email/i).fill(email);
  await page.getByLabel(/^password$/i).fill(newPassword);
  await page.getByRole("button", { name: /^sign in$/i }).click();

  await expect(page).toHaveURL(/\/my-time/);
});
