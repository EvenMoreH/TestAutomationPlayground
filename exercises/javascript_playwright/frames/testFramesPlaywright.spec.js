import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { FramesPage } from "../frames/framesPlaywright";

test("click and validate outer and inner buttons", async ({ page }) => {
    const framesPage = new FramesPage(page);
    const navbar = new Navbar(page);

    await framesPage.openExercisePage();
    await navbar.pageLoaded();

    const resultPrefix = "Button pressed: ";

    await framesPage.clickOuterEditButton();
    await expect(framesPage.outerResult).toHaveText(resultPrefix + "Edit");

    await framesPage.clickOuterSubmitButton();
    await expect(framesPage.outerResult).toHaveText(resultPrefix + "Submit");

    await framesPage.clickOuterClickMeButton();
    await expect(framesPage.outerResult).toHaveText(resultPrefix + "Click me");

    await framesPage.clickOuterPrimaryButton();
    await expect(framesPage.outerResult).toHaveText(resultPrefix + "Primary");

    await framesPage.clickInnerEditButton();
    await expect(framesPage.innerResult).toHaveText(resultPrefix + "Edit");

    await framesPage.clickInnerSubmitButton();
    await expect(framesPage.innerResult).toHaveText(resultPrefix + "Submit");

    await framesPage.clickInnerClickMeButton();
    await expect(framesPage.innerResult).toHaveText(resultPrefix + "Click me");

    await framesPage.clickInnerPrimaryButton();
    await expect(framesPage.innerResult).toHaveText(resultPrefix + "Primary");
});
