from playwright.sync_api import Page


class DynamicTable:
    def __init__(self, page: Page):
        """Store the Playwright page and ARIA table locators."""
        self.page = page
        self.column = page.get_by_role("columnheader")
        self.row = page.get_by_role("row")
        self.cell = page.get_by_role("cell")
        self.banner = page.locator(".bg-warning")


    def open(self) -> None:
        """Open the Dynamic Table exercise page."""
        self.page.goto("http://uitestingplayground.com/dynamictable")


    def _get_column_index(self, column: str) -> int:
        """Return the zero-based index of the given column header."""
        headers: list[str] = self.column.all_text_contents()
        return headers.index(column)


    def get_cell_value(self, column: str, cell: str) -> str:
        """Return the value at the intersection of a given column and row."""
        column_index = self._get_column_index(column)
        rows = self.row.all()
        for row in rows:
            cells = row.get_by_role("cell").all_text_contents()
            if cells and cells[0] == cell:
                return cells[column_index]
        raise ValueError(f"{cell} row not found")

    def get_banner_value(self) -> str:
        return self.banner.text_content() or ""
