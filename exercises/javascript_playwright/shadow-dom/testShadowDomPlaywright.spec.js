import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { ShadowDOMPage } from "../shadow-dom/shadowDomPlaywright";

test("generate guide and verify it", async ({ page }) => {
    const shadowDOMPage = new ShadowDOMPage(page);
    const navbar = new Navbar(page);

    await shadowDOMPage.openExercisePage();
    await navbar.pageLoaded();

    await shadowDOMPage.clickGenerateGuidButton();
    await shadowDOMPage.clickCopyButton();

    const clipboardText = await page.evaluate(() =>
        navigator.clipboard.readText(),
    );
    const guidText = await shadowDOMPage.readGuidField();
    expect(clipboardText).toEqual(guidText);
});
