import { test, expect } from "@playwright/test";
import { Navbar } from "../navbar";
import { DynamicTablePage } from "../dynamic-table/dynamicTablePlaywright";

test("get chrome CPU usage value", async ({ page }) => {
    const dynamicTablePage = new DynamicTablePage(page);
    const navbar = new Navbar(page);

    await dynamicTablePage.openExercisePage();
    await navbar.pageLoaded();

    const tableValue = await dynamicTablePage.getCellValue("CPU", "Chrome");
    const bannerValue = await dynamicTablePage.getMessageBannerText();
    expect(bannerValue).toBe(`Chrome CPU: ${tableValue}`);
});
