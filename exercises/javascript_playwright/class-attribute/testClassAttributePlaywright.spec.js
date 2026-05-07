import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { ClassAttrPage } from "../class-attribute/classAttributePlaywright";

test("click primary button and accept alert", async ({ page }) => {
    const classAttrPage = new ClassAttrPage(page);
    const navbar = new Navbar(page);

    await classAttrPage.openExercisePage();
    await navbar.pageLoaded();

    const result = await classAttrPage.clickPrimaryButtonAndAcceptAlert();
    expect(result).toBe("Primary button pressed");
});
