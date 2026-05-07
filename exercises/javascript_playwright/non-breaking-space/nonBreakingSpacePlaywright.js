export class NbspPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.button = page.getByRole("button", { name: /^My\s+Button$/ });
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/nbsp");
    }

    async clickButton() {
        await this.button.click();
    }
}
