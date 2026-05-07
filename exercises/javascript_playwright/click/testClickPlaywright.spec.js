import { test, expect } from "@playwright/test";
import { ClickPage } from "../click/clickPlaywright";
import { Navbar } from "../navbar";

test("click button", async ({ page }) => {
    const clickPage = new ClickPage(page);
    const navbar = new Navbar(page);

    await clickPage.openExercisePage();
    await navbar.pageLoaded();

    await clickPage.clickButton();
    await expect(clickPage.button).toContainClass("btn-success");
});
