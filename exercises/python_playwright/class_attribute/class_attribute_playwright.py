from playwright.sync_api import Dialog, Page


class ClassAttribute:
    def __init__(self, page: Page):
        """Initialize the page object with Playwright locators."""
        self.page = page
        self.button = page.locator("button.btn-primary")

    def open(self) -> None:
        """Navigate to the Class Attribute exercise page."""
        self.page.goto("http://uitestingplayground.com/classattr")

    def click_primary_button(self) -> str:
        """Click the primary button and return the following alert message."""
        dialog_msg = ""

        def dialog_handler(dialog: Dialog) -> None:
            nonlocal dialog_msg
            dialog_msg = dialog.message
            dialog.accept()

        self.page.once("dialog", dialog_handler)
        self.button.click()

        return dialog_msg
