from playwright.sync_api import Page


class DynamicID:
    def __init__(self, page: Page):
        """Store the Playwright page and the dynamic button locator."""
        self.page = page
        self.button = page.get_by_role("button", name="Button with Dynamic ID")


    def open(self) -> None:
        """Open the Dynamic ID exercise page."""
        self.page.goto("http://uitestingplayground.com/dynamicid")


    def click_dynamic_button(self) -> None:
        """Click the button with the dynamic ID."""
        self.button.click()