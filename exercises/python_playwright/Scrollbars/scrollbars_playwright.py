from playwright.sync_api import Page


class ScrollbarsPage:
    def __init__(self, page: Page):
        self.page = page
        self.hiding_button = page.get_by_role("button", name="Hiding Button")

    def open(self) -> None:
        self.page.goto("http://uitestingplayground.com/scrollbars")

    def click_hiding_button(self) -> None:
        self.hiding_button.scroll_into_view_if_needed()
        self.hiding_button.click()