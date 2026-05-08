import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { ProgressBarPage } from "../progress-bar/progressBarPlaywright";

test("start progress bar and stop it at 75%", async ({ page }) => {
    const progressBarPage = new ProgressBarPage(page);
    const navbar = new Navbar(page);

    await progressBarPage.openExercisePage();
    await navbar.pageLoaded();

    await progressBarPage.clickStartButton();
    await progressBarPage.clickStopButtonAt(75);

    const resultText = await progressBarPage.getResultText();
    expect(resultText).toContain("Result: 0");
});
