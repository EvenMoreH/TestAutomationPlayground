export class FileUploadPage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.iframe = page.frameLocator("iframe");
        this.fileInput = this.iframe.locator("#browse");
        this.uploadedFile = this.iframe.locator(".file-item");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/upload");
    }

    async uploadFiles(files) {
        await this.fileInput.setInputFiles(files);
    }

    async getUploadedFilesNames() {
        return await this.uploadedFile.allTextContents();
    }
}
