import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { DisabledInputPage } from "../disabled-input/disabledInputPlaywright";

const testInputs = ["Playwright", "test", "12345", "!@#$%"];

testInputs.forEach((input) => {
    test(`input text "${input}" into input field after it gets enabled`, async ({
        page,
    }) => {
        const disabledInputPage = new DisabledInputPage(page);
        const navbar = new Navbar(page);

        await disabledInputPage.openExercisePage();
        await navbar.pageLoaded();

        await disabledInputPage.clickEnableButton();
        await disabledInputPage.typeInInputField(input);

        const status = await disabledInputPage.getStatus();
        expect(status).toBe(`Value changed to: ${input}`);
    });
});
