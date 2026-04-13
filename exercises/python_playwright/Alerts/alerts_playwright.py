from playwright.sync_api import Dialog, Page


class AlertsPage:
    def __init__(self, page: Page) -> None:
        """Initialize the page object with Playwright locators."""
        self.page = page
        self.alert_button = page.get_by_role("button", name="Alert")
        self.confirm_button = page.get_by_role("button", name="Confirm")
        self.prompt_button = page.get_by_role("button", name="Prompt")

    def open(self) -> None:
        """Navigate to the Alerts exercise page."""
        self.page.goto("http://uitestingplayground.com/alerts")

    def click_alert(self) -> None:
        """Accept the alert dialog triggered by the Alert button."""
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.alert_button.click()

    def click_confirm(self, accept: bool = True) -> str:
        """Handle the confirm dialog and return the follow-up alert message."""
        self.page.once("dialog", lambda dialog: dialog.accept() if accept else dialog.dismiss())
        self.confirm_button.click()

        second_alert_box: Dialog = self.page.wait_for_event("dialog", timeout=5000)
        message = second_alert_box.message
        second_alert_box.accept()
        return message

    def click_prompt(self, input_text: str) -> str:
        """Submit prompt input and return the follow-up alert message."""
        self.page.once("dialog", lambda dialog: dialog.accept(input_text))
        self.prompt_button.click()

        second_alert_box: Dialog = self.page.wait_for_event("dialog", timeout=5000)
        message = second_alert_box.message
        second_alert_box.accept()
        return message
