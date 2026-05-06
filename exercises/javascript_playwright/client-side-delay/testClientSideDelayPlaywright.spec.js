import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { ClientSideDelayPage } from "../client-side-delay/clientSideDelayPlaywright";

test("click button triggering client side logic", async ({ page }) => {
    const navbar = new Navbar(page);
    const clientSideDelayPage = new ClientSideDelayPage(page);

    await clientSideDelayPage.openPage();
    await navbar.pageLoaded();

    await clientSideDelayPage.clickButtonTriggeringClientSideLogic();
    await expect(clientSideDelayPage.successMessage).toHaveText(
        "Data calculated on the client side.",
        { timeout: 25000 },
    );
});
