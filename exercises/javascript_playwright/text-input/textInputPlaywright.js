export class TextInputPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.textInput = page.locator("#newButtonName");
        this.button = page.locator("#updatingButton");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/textinput");
    }

    async fillNewButtonName(text) {
        await this.textInput.fill(text);
    }

    async clickButton() {
        await this.button.click();
    }

    async readButtonNameText() {
        return await this.button.textContent();
    }
}
