export class AlertsPage {
    /**
     *
     * @param {import(@playwright).Page} page
     */
    constructor(page) {
        this.page = page;
        this.alertButton = page.locator("#alertButton");
        this.confirmButton = page.locator("#confirmButton");
        this.promptButton = page.locator("#promptButton");
    }
    async openPage() {
        await this.page.goto("http://uitestingplayground.com/alerts");
    }

    async clickAlertButton() {
        await this.page.once("dialog", (dialog) => dialog.accept());
        await this.alertButton.click();
    }

    async clickConfirmButton(decision) {
        await this.page.once("dialog", (dialog) => {
            decision ? dialog.accept() : dialog.dismiss();
        });
        await this.confirmButton.click();
    }

    async clickPromptButton(input) {
        await this.page.once("dialog", (dialog) => dialog.accept(input));
        await this.promptButton.click();
    }

    async getFollowupAlert() {
        const dialog = await this.page.waitForEvent("dialog", {
            timeout: 5000,
        });
        const alertMessage = dialog.message();
        dialog.accept();

        return alertMessage;
    }
}
