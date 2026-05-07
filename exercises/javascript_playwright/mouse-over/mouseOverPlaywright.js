export class MouseOverPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.clickMeLink = page.getByTitle("Click me");
        this.clickMeLinkActive = page.getByTitle("Active Link");
        this.linkButton = page.getByTitle("Link Button");
        this.clickMeCounter = page.locator("#clickCount");
        this.linkButtonCounter = page.locator("#clickButtonCount");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/mouseover");
    }

    async hoverClickMeLink() {
        await this.clickMeLink.hover();
    }

    async hoverLinkButton() {
        await this.linkButton.hover();
    }

    async doubleClickClickMeLink() {
        await this.clickMeLinkActive.dblclick();
    }

    async doubleClickLinkButton() {
        await this.linkButton.dblclick();
    }
}
