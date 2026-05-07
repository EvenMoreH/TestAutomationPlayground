import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { MouseOverPage } from "../mouse-over/mouseOverPlaywright";

test("hover over click me link and validate it can be double clicked", async ({
    page,
}) => {
    const mouseOverPage = new MouseOverPage(page);
    const navbar = new Navbar(page);

    await mouseOverPage.openExercisePage();
    await navbar.pageLoaded();

    await mouseOverPage.hoverClickMeLink();
    await mouseOverPage.doubleClickClickMeLink();
    await expect(mouseOverPage.clickMeCounter).toHaveText("2");
});

test("hover over link button and validate it can be double clicked", async ({
    page,
}) => {
    const mouseOverPage = new MouseOverPage(page);
    const navbar = new Navbar(page);

    await mouseOverPage.openExercisePage();
    await navbar.pageLoaded();

    await mouseOverPage.hoverLinkButton();
    await mouseOverPage.doubleClickLinkButton();
    await expect(mouseOverPage.linkButtonCounter).toHaveText("2");
});
