export class OverlappedElementPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.nameInput = page.locator("#name");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/overlapped");
    }

    async scrollToNameInput() {
        await this.nameInput.click();
        await this.nameInput.evaluate((element) => (element.scrollTop += 100));
    }

    async fillNameInput(name) {
        await this.nameInput.fill(name);
    }

    async readNameInputValue() {
        return await this.nameInput.inputValue();
    }
}
