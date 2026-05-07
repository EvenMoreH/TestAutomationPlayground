import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { HiddenLayersPage } from "../hidden-layers/hiddenLayersPlaywright";

test("validate that green button can be clicked only once", async ({
    page,
}) => {
    const hiddenLayersPage = new HiddenLayersPage(page);
    const navbar = new Navbar(page);

    await hiddenLayersPage.openExercisePage();
    await navbar.pageLoaded();

    await hiddenLayersPage.clickGreenButton();
    await expect(hiddenLayersPage.isGreenButtonCovered()).resolves.toBeTruthy();
});
