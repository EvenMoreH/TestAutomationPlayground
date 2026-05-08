export class ScrollbarsPage {
    /**
     *
     * @param {import("@playwright/test").Page} page
     */
    constructor(page) {
        this.page = page;
        this.button = page.locator("#hidingButton");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/scrollbars");
    }

    async clickButton() {
        await this.button.scrollIntoViewIfNeeded();
        await this.button.click();
    }
}
