import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { AnimatedButtonPage } from "../animated-button/animatedButtonPlaywright";

test("click animated button after animation ends", async ({ page }) => {
    const animatedButtonPage = new AnimatedButtonPage(page);
    const navbar = new Navbar(page);

    await animatedButtonPage.openExercisePage();
    await navbar.pageLoaded();

    await animatedButtonPage.clickStartButton();
    await animatedButtonPage.clickAnimatedButton();
    await expect(animatedButtonPage.status).toHaveText(
        "Moving Target clicked. It's class name is 'btn btn-primary'",
        { timeout: 15000 },
    );
});
