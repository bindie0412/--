import { test, expect } from '@playwright/test';

test('basic verification', async ({ page }) => {
  await page.goto('http://localhost:3000');

  await expect(page.locator('text=Focus Stats')).toBeVisible();
  await expect(page.locator('text=To-Do')).toBeVisible();
  await page.screenshot({ path: 'dashboard.png', fullPage: true });

  await page.click('button[title="Enter Focus Mode"]');
  await expect(page.locator('text=Deep Work in Progress')).toBeVisible();
  await page.screenshot({ path: 'focus-mode.png', fullPage: true });
});
