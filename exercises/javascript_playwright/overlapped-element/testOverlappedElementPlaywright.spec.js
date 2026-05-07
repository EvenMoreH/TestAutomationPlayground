import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { OverlappedElementPage } from "../overlapped-element/overlappedElementPlaywright";

const testInput = "John Doe";

test("scroll name field into view and fill it", async ({ page }) => {
    const overlappedElementPage = new OverlappedElementPage(page);
    const navbar = new Navbar(page);

    await overlappedElementPage.openExercisePage();
    await navbar.pageLoaded();

    await overlappedElementPage.scrollToNameInput();
    await overlappedElementPage.fillNameInput(testInput);
    const nameInputValue = await overlappedElementPage.readNameInputValue();
    expect(nameInputValue).toBe(testInput);
});
