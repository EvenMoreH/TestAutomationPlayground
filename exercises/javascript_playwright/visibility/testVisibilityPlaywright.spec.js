import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { VisibilityPage } from "../visibility/visibilityPlaywright";

const buttons = [
    ["Removed Button", "removedButton"],
    ["Zero Width Button", "zeroWidthButton"],
    ["Overlapped Button", "overlappedButton"],
    ["Zero Opacity Button", "zeroOpacityButton"],
    ["Hidden Button", "hiddenButton"],
    ["Not Displayed Button", "noneButton"],
    ["Offscreen Button", "offscreenButton"],
];

buttons.forEach(([buttonName, buttonProperty]) => {
    test(`check user visibility of ${buttonName}`, async ({ page }) => {
        const visibilityPage = new VisibilityPage(page);
        const navbar = new Navbar(page);

        await visibilityPage.openExercisePage();
        await navbar.pageLoaded();
        await visibilityPage.clickHideButton();

        const button = visibilityPage[buttonProperty];
        const isInvisible =
            await visibilityPage.checkIfButtonIsInvisibleToUser(button);

        expect(isInvisible).toBe(true);
    });
});
