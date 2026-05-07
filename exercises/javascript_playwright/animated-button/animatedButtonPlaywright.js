import { expect } from "@playwright/test";

export class AnimatedButtonPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.startButton = page.locator("#animationButton");
        this.animatedButton = page.locator("#movingTarget");
        this.status = page.locator("#opstatus");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/animation");
    }

    async clickStartButton() {
        await this.startButton.click();
    }

    async clickAnimatedButton() {
        await expect(this.animatedButton).not.toContainClass("spin", {
            timeout: 15000,
        });
        await this.animatedButton.click();
    }
}
