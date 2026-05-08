import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { TextInputPage } from "../text-input/textInputPlaywright";

const buttonNames = ["Submit", "Click Me", "Press Here", "12345", "!@#$%", " "];

buttonNames.forEach((testButtonName) => {
    test(`provide a button name, click the button and verify the name has been updated to ${testButtonName}`, async ({
        page,
    }) => {
        const textInputPage = new TextInputPage(page);
        const navbar = new Navbar(page);

        await textInputPage.openExercisePage();
        await navbar.pageLoaded();

        await textInputPage.fillNewButtonName(testButtonName);
        await textInputPage.clickButton();

        const newButtonName = await textInputPage.readButtonNameText();
        expect(newButtonName).toBe(testButtonName);
    });
});
