export class ClientSideDelayPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.delayedButton = page.getByRole("button", {
            name: "Button Triggering Client Side Logic",
        });
        this.successMessage = page.locator(".bg-success");
    }
    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/clientdelay");
    }

    async clickButtonTriggeringClientSideLogic() {
        await this.delayedButton.click();
    }
}
