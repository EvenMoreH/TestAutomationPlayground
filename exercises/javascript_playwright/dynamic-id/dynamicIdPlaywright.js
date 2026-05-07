export class DynamicIdPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.button = page.getByRole("button", {
            name: "Button with Dynamic ID",
        });
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/dynamicid");
    }

    async clickButton() {
        await this.button.click();
    }
}
