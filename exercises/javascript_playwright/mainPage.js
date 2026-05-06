export class MainPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.loadDelayLink = page.getByRole("link", { name: "Load Delay" });
    }

    async openMainPage() {
        await this.page.goto("http://uitestingplayground.com/");
    }

    async goToLoadDelayExercisePage() {
        await this.loadDelayLink.click();
    }
}
