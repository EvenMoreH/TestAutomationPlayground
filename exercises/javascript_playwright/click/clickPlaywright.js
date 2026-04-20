export class ClickPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.button = page.locator("#badButton");
    }

    async openPage() {
        await this.page.goto("http://uitestingplayground.com/click");
    }

    async clickButton() {
        await this.button.click();
    }
}
