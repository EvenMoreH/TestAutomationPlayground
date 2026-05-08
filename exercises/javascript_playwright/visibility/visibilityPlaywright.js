export class VisibilityPage {
    /**
     *
     * @param {import("@playwright/test").Page} page
     */
    constructor(page) {
        this.page = page;
        this.hideButton = page.locator("#hideButton");
        this.removedButton = page.locator("#removedButton");
        this.zeroWidthButton = page.locator("#zeroWidthButton");
        this.overlappedButton = page.locator("#overlappedButton");
        this.zeroOpacityButton = page.locator("#transparentButton");
        this.hiddenButton = page.locator("#invisibleButton");
        this.noneButton = page.locator("#notdisplayedButton");
        this.offscreenButton = page.locator("#offscreenButton");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/visibility");
    }

    async clickHideButton() {
        await this.hideButton.click();
    }

    async checkIfButtonIsInvisibleToUser(button) {
        // built in method
        if (!(await button.isVisible())) {
            return true;
        }

        // check opacity
        const opacity = await button.evaluate((el) => {
            return window.getComputedStyle(el).opacity;
        });
        if (opacity === "0") {
            return true;
        }

        // check if overlapped
        const overlapped = await button.evaluate((el) => {
            const rect = el.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            const elementAtPoint = document.elementFromPoint(centerX, centerY);
            return !el.contains(elementAtPoint) && elementAtPoint !== el;
        });
        if (overlapped) {
            return true;
        }

        // check if offscreen
        const offscreen = await button.evaluate((el) => {
            const rect = el.getBoundingClientRect();
            return (
                rect.bottom < 0 ||
                rect.right < 0 ||
                rect.left > window.innerWidth ||
                rect.top > window.innerHeight
            );
        });
        if (offscreen) {
            return true;
        }

        return false;
    }
}
