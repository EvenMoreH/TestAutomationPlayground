import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { NbspPage } from "../non-breaking-space/nonBreakingSpacePlaywright";

test("click button with non-breaking space ", async ({ page }) => {
    const nbspPage = new NbspPage(page);
    const navbar = new Navbar(page);

    await nbspPage.openExercisePage();
    await navbar.pageLoaded();

    await nbspPage.clickButton();
});
