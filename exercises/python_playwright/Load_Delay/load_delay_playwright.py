from playwright.sync_api import Page


class DelayMainPage:
    """Page object for the load-delay landing page."""

    def __init__(self, page: Page):
        """Initialize the landing page locators."""
        self.page = page
        self.link = page.get_by_role("link", name="Load Delay")

    def open(self) -> None:
        """Open the main playground page."""
        self.page.goto("http://uitestingplayground.com")

    def click_link(self) -> None:
        """Click the Load Delay link."""
        self.link.click()


class DelayExercisePage:
    """Page object for the load-delay exercise page."""

    def __init__(self, page: Page):
        """Initialize the exercise page locators."""
        self.page = page
        self.button = page.locator(".btn-primary")

    def click_button(self) -> None:
        """Click the target button."""
        self.button.click()