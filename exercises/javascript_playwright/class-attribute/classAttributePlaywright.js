export class ClassAttrPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.button = page.locator(".btn-primary");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/classattr");
    }

    async clickPrimaryButtonAndAcceptAlert() {
        let dialogMessage = "";

        this.page.once("dialog", async (dialog) => {
            dialogMessage = dialog.message();
            await dialog.accept();
        });

        await this.button.click();

        return dialogMessage;
    }
}
