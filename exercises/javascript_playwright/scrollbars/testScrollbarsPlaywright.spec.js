import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { ScrollbarsPage } from "../scrollbars/scrollbarsPlaywright";

test("scroll button into view and click it", async ({ page }) => {
    const scrollbarsPage = new ScrollbarsPage(page);
    const navbar = new Navbar(page);

    await scrollbarsPage.openExercisePage();
    await navbar.pageLoaded();

    await scrollbarsPage.clickButton();
});
