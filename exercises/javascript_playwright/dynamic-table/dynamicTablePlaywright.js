export class DynamicTablePage {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.messageBanner = page.locator(".bg-warning");
        this.column = page.getByRole("columnheader");
        this.row = page.getByRole("row");
        this.cel = page.getByRole("cell");
    }

    async openExercisePage() {
        await this.page.goto("http://uitestingplayground.com/dynamictable");
    }

    async getColumnIndex(columnName) {
        const columns = await this.column.allTextContents();
        return columns.indexOf(columnName);
    }

    async getCellValue(columnName, rowName) {
        const columnIndex = await this.getColumnIndex(columnName);
        if (columnIndex === -1) {
            throw new Error(`Column "${columnName}" not found`);
        }

        const rows = await this.row.all();

        for (const row of rows) {
            const cells = await row.getByRole("cell").allTextContents();
            if (cells[0] === rowName) {
                return cells[columnIndex];
            }
        }
        throw new Error(`Row "${rowName}" not found`);
    }

    async getMessageBannerText() {
        return await this.messageBanner.textContent();
    }
}
