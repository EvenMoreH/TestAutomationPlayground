from playwright.sync_api import Page


class ScrollbarsPage:
    def __init__(self, page: Page):
        """Page object for the Scrollbars exercise."""
        self.page = page
        self.hiding_button = page.get_by_role("button", name="Hiding Button")

    def open(self) -> None:
        """Open the Scrollbars exercise page."""
        self.page.goto("http://uitestingplayground.com/scrollbars")

    def click_hiding_button(self) -> None:
        """Scroll to the hidden button and click it."""
        self.hiding_button.scroll_into_view_if_needed()
        self.hiding_button.click()