export class VerifyTextPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.text = page.locator(
            "//span[normalize-space(.)='Welcome UserName!']",
        );
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/verifytext");
    }
}
