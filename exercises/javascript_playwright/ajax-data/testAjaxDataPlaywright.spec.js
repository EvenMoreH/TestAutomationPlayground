import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { AJAXDataPage } from "../ajax-data/ajaxDataPlaywright";

test("click AJAX button and check for success message", async ({ page }) => {
    const ajaxDataPage = new AJAXDataPage(page);
    const navbar = new Navbar(page);

    await ajaxDataPage.openPage();
    await navbar.pageLoaded();

    await ajaxDataPage.clickAJAXButton();
    await expect(ajaxDataPage.successMessage).toContainText(
        "Data loaded with AJAX get request.",
        { timeout: 25000 },
    );
});
