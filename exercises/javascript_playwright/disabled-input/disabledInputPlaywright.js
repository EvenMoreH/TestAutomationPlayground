export class DisabledInputPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.button = page.locator("#enableButton");
        this.inputField = page.locator("#inputField");
        this.status = page.locator("#opstatus");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/disabledinput");
    }

    async clickEnableButton() {
        await this.button.click();
    }

    async typeInInputField(text) {
        await this.inputField.fill(text, { timeout: 10000 });
        await this.inputField.press("Enter");
    }

    async getStatus() {
        return await this.status.textContent();
    }
}
