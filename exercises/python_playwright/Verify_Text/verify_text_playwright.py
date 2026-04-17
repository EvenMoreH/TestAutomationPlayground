from playwright.sync_api import Page


class VerifyTextPage:
    def __init__(self, page: Page):
        """Store page and locators used by the exercise."""
        self.page = page
        self.welcome_msg = page.locator("//div[normalize-space(.)='Welcome UserName!']")

    def open(self) -> None:
        """Open the Verify Text exercise page."""
        self.page.goto("http://uitestingplayground.com/verifytext")

    def find_and_return_welcome_message(self) -> str:
        """Return the welcome message text from the page."""
        return self.welcome_msg.inner_text()