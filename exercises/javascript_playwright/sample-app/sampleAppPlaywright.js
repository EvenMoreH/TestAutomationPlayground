export class SampleAppPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.nameInput = page.locator("[name='UserName']");
        this.passwordInput = page.locator("[name='Password']");
        this.loginButton = page.getByRole("button", { name: "Log In" });
        this.logoutButton = page.getByRole("button", { name: "Log Out" });
        this.loginStatus = page.locator("#loginstatus");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/sampleapp");
    }

    async login(username, password) {
        await this.nameInput.fill(username);
        await this.passwordInput.fill(password);
        await this.loginButton.click();
    }

    async logout() {
        await this.logoutButton.click();
    }

    async getLoginStatus() {
        return await this.loginStatus.textContent();
    }
}
