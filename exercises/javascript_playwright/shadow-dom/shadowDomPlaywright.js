export class ShadowDOMPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.guidField = page.locator("#editField");
        this.generateButton = page.locator("#buttonGenerate");
        this.copyButton = page.locator("#buttonCopy");
    }

    async openExercisePage() {
        await this.page.goto("https://uitestingplayground.com/shadowdom");
    }

    async clickGenerateGuidButton() {
        await this.generateButton.click();
    }

    async clickCopyButton() {
        await this.copyButton.click();
    }

    async readGuidField() {
        return await this.guidField.inputValue();
    }
}
