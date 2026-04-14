from playwright.sync_api import Page


class ClientSideDelay:
    def __init__(self, page: Page):
        """Store the Playwright page and relevant locators."""
        self.page = page
        self.button = page.get_by_role("button", name="Button Triggering Client Side Logic")
        self.success_label = page.locator(".bg-success")


    def open(self) -> None:
        """Open the Client Side Delay exercise page."""
        self.page.goto("http://uitestingplayground.com/clientdelay")


    def trigger_client_logic(self) -> None:
        """Trigger the delayed client-side behavior."""
        self.button.click()