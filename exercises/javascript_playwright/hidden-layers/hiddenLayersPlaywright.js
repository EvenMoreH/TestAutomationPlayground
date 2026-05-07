export class HiddenLayersPage {
    /**
     *
     * @param {import('playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.greenButton = page.locator("#greenButton");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/hiddenlayers");
    }

    async clickGreenButton() {
        await this.greenButton.click();
    }

    async isGreenButtonCovered() {
        return await this.greenButton.evaluate((button) => {
            const buttonRect = button.getBoundingClientRect();
            const centerX = buttonRect.left + buttonRect.width / 2;
            const centerY = buttonRect.top + buttonRect.height / 2;

            const topElement = document.elementFromPoint(centerX, centerY);
            return topElement !== button;
        });
    }
}
