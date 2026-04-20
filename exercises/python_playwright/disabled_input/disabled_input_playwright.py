from playwright.sync_api import Page


class DisabledInput:
    def __init__(self, page: Page):
        """Store the Playwright page and relevant locators."""
        self.page = page
        self.input_field = page.get_by_placeholder("Change me...")
        self.button = page.locator("#enableButton")
        self.status_field = page.locator("#opstatus")


    def open(self) -> None:
        """Open the Disabled Input exercise page."""
        self.page.goto("http://uitestingplayground.com/disabledinput")


    def click_enable_edit_button(self) -> None:
        """Click the button that enables the input field."""
        self.button.click()


    def input_text(self, text: str) -> None:
        """Type text into the input once it becomes enabled. Confirm wit Enter."""
        while self.input_field.is_disabled():
            self.input_field.fill(text)
            self.input_field.press("Enter")