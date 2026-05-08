import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { VerifyTextPage } from "../verify-text/verifyTextPlaywright";

test("find text on the page", async ({ page }) => {
    const verifyTextPage = new VerifyTextPage(page);
    const navbar = new Navbar(page);

    await verifyTextPage.openExercisePage();
    await navbar.pageLoaded();

    const textToFind = "Welcome UserName!";
    await expect(verifyTextPage.text).toHaveText(textToFind, {
        useInnerText: true,
    });
});
