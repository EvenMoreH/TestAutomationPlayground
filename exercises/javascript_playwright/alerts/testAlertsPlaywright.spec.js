import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { AlertsPage } from "../alerts/alertsPlaywright";

test("confirm alert for alert button", async ({ page }) => {
    const alertsPage = new AlertsPage(page);
    const navbar = new Navbar(page);

    await alertsPage.openPage();
    await navbar.pageLoaded();

    await alertsPage.clickAlertButton();
});

test("confirm alert for confirm button", async ({ page }) => {
    const alertsPage = new AlertsPage(page);
    const navbar = new Navbar(page);

    await alertsPage.openPage();
    await navbar.pageLoaded();

    await alertsPage.clickConfirmButton(true);
    const result = await alertsPage.getFollowupAlert();
    expect(result).toBe("Yes");
});

test("dismiss alert for confirm button", async ({ page }) => {
    const alertsPage = new AlertsPage(page);
    const navbar = new Navbar(page);

    await alertsPage.openPage();
    await navbar.pageLoaded();

    await alertsPage.clickConfirmButton(false);
    const result = await alertsPage.getFollowupAlert();
    expect(result).toBe("No");
});

const promptInputs = [
    "cats",
    "dogs",
    "playwright",
    "Test",
    "12345",
    "!@#$%",
    "",
];
promptInputs.forEach((input) => {
    test(`enter text "${input}" in prompt alert`, async ({ page }) => {
        const alertsPage = new AlertsPage(page);
        const navbar = new Navbar(page);

        await alertsPage.openPage();
        await navbar.pageLoaded();

        await alertsPage.clickPromptButton(input);
        const result = await alertsPage.getFollowupAlert();
        expect(result).toBe(`User value: ${input}`);
    });
});
