import { test } from "@playwright/test";
import { Navbar } from "../navbar";
import { MainPage } from "../mainPage";
import { LoadDelayPage } from "../load-delay/loadDelayPlaywright";

test("click button appearing after delay", async ({ page }) => {
    const mainPage = new MainPage(page);
    const navbar = new Navbar(page);
    const loadDelayPage = new LoadDelayPage(page);

    await mainPage.openMainPage();
    await navbar.pageLoaded();

    await mainPage.goToLoadDelayExercisePage();
    await navbar.pageLoaded();
    await loadDelayPage.clickButtonAppearingAfterDelay();
});
