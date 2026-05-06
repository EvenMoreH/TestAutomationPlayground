export class AJAXDataPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.AJAXButton = page.locator("#ajaxButton");
        this.successMessage = page.locator(".bg-success");
    }
    async openPage() {
        await this.page.goto("http://uitestingplayground.com/ajax");
    }

    async clickAJAXButton() {
        await this.AJAXButton.click();
    }
}
