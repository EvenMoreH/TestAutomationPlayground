export class FramesPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.outerFrame = page.frameLocator("#frame-outer");
        this.outerEditButton = this.outerFrame.locator("[data-action='edit']");
        this.outerSubmitButton = this.outerFrame.getByRole("button", {
            name: "Submit",
        });
        this.outerClickMeButton = this.outerFrame.getByText("Click Me");
        this.outerPrimaryButton = this.outerFrame.locator(".btn-class", {
            name: "Primary",
        });

        this.innerFrame = this.outerFrame.frameLocator("#frame-inner");
        this.innerEditButton = this.innerFrame.locator("[data-action='edit']");
        this.innerSubmitButton = this.innerFrame.getByRole("button", {
            name: "Submit",
        });
        this.innerClickMeButton = this.innerFrame.getByText("Click Me");
        this.innerPrimaryButton = this.innerFrame.locator(".btn-class", {
            name: "Primary",
        });

        this.outerResult = this.outerFrame.locator("#result");
        this.innerResult = this.innerFrame.locator("#result");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/frames");
    }

    async clickOuterEditButton() {
        await this.outerEditButton.click();
    }

    async clickOuterSubmitButton() {
        await this.outerSubmitButton.click();
    }

    async clickOuterClickMeButton() {
        await this.outerClickMeButton.click();
    }

    async clickOuterPrimaryButton() {
        await this.outerPrimaryButton.click();
    }

    async clickInnerEditButton() {
        await this.innerEditButton.click();
    }

    async clickInnerSubmitButton() {
        await this.innerSubmitButton.click();
    }

    async clickInnerClickMeButton() {
        await this.innerClickMeButton.click();
    }

    async clickInnerPrimaryButton() {
        await this.innerPrimaryButton.click();
    }
}
