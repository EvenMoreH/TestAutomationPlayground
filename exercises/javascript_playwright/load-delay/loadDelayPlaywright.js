export class LoadDelayPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.delayedButton = page.getByRole("button", {
            name: "Button Appearing After Delay",
        });
    }

    async clickButtonAppearingAfterDelay() {
        await this.delayedButton.click();
    }
}
