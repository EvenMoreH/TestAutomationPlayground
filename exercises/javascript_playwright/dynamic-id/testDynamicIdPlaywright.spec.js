import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { DynamicIdPage } from "../dynamic-id/dynamicIdPlaywright";

test("click button with dynamic id", async ({ page }) => {
    const dynamicIdPage = new DynamicIdPage(page);
    const navbar = new Navbar(page);

    await dynamicIdPage.openExercisePage();
    await navbar.pageLoaded();

    await dynamicIdPage.clickButton();
});
