from playwright.sync_api import Page


class Click:
    def __init__(self, page: Page):
        """Store the Playwright page and button locator."""
        self.page = page
        self.button = page.locator("#badButton")


    def open(self) -> None:
        """Open the Click exercise page."""
        self.page.goto("http://uitestingplayground.com/click")


    def click_button(self) -> None:
        """Click the target button."""
        self.button.click()