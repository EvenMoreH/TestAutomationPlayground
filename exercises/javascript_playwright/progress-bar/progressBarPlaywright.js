import { expect } from "@playwright/test";

export class ProgressBarPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.startButton = page.locator("#startButton");
        this.stopButton = page.locator("#stopButton");
        this.progressBar = page.locator("#progressBar");
        this.result = page.locator("#result");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/progressbar");
    }

    async clickStartButton() {
        await this.startButton.click();
    }

    async getProgressBarValue() {
        const value = await this.progressBar.getAttribute("aria-valuenow");
        return Number(value);
    }

    async clickStopButtonAt(percentage) {
        await expect
            .poll(async () => await this.getProgressBarValue(), {
                timeout: 30000,
                intervals: [50, 50, 5, 5],
            })
            .toBe(percentage);
        await this.stopButton.click();
    }

    async getResultText() {
        return await this.result.textContent();
    }
}
