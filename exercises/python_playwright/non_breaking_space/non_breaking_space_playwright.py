from playwright.sync_api import Page
import re


class NBSPPage:
    """Page object for the non-breaking space exercise."""

    def __init__(self, page: Page):
        """Initialize the page and target button locator."""
        self.page = page
        self.button = page.get_by_role("button", name=re.compile(r"My\s*Button"))

    def open(self) -> None:
        """Open the exercise page."""
        self.page.goto("http://uitestingplayground.com/nbsp")

    def click_button(self) -> None:
        """Click the target button."""
        self.button.click()