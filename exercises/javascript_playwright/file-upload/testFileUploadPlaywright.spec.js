import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { FileUploadPage } from "../file-upload/fileUploadPlaywright";
import { testFiles, getFilePaths } from "../file-upload/testData";

const dir = "exercises/javascript_playwright/file-upload/";
const files = getFilePaths(dir);

test("upload files and verify file name", async ({ page }) => {
    const fileUploadPage = new FileUploadPage(page);
    const navbar = new Navbar(page);

    await fileUploadPage.openExercisePage();
    await navbar.pageLoaded();

    await fileUploadPage.uploadFiles(files);
    const uploadedFilesNames = await fileUploadPage.getUploadedFilesNames();
    expect(uploadedFilesNames).toContain(...uploadedFilesNames);
});
