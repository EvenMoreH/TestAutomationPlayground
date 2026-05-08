import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { SampleAppPage } from "../sample-app/sampleAppPlaywright";

test("login with valid credentials and then logout", async ({ page }) => {
    const sampleAppPage = new SampleAppPage(page);
    const navbar = new Navbar(page);

    await sampleAppPage.openExercisePage();
    await navbar.pageLoaded();

    await sampleAppPage.login("test", "pwd");
    let loginStatus = await sampleAppPage.getLoginStatus();
    expect(loginStatus).toBe("Welcome, test!");

    await sampleAppPage.logout();
    loginStatus = await sampleAppPage.getLoginStatus();
    expect(loginStatus).toBe("User logged out.");
});

test("login with invalid credentials", async ({ page }) => {
    const sampleAppPage = new SampleAppPage(page);
    const navbar = new Navbar(page);

    await sampleAppPage.openExercisePage();
    await navbar.pageLoaded();

    await sampleAppPage.login("invalidUser", "invalidPwd");
    const loginStatus = await sampleAppPage.getLoginStatus();
    expect(loginStatus).toBe("Invalid username/password");
});

test("login with empty credentials", async ({ page }) => {
    const sampleAppPage = new SampleAppPage(page);
    const navbar = new Navbar(page);

    await sampleAppPage.openExercisePage();
    await navbar.pageLoaded();

    await sampleAppPage.login("", "");
    const loginStatus = await sampleAppPage.getLoginStatus();
    expect(loginStatus).toBe("Invalid username/password");
});
