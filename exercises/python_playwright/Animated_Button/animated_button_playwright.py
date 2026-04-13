from playwright.sync_api import Page, expect


class AnimatedButton:
    def __init__(self, page: Page):
        """Initialize the page object with Playwright locators."""
        self.page = page
        self.start_button = page.get_by_role("button", name="Start Animation")
        self.target_button = page.locator("#movingTarget")
        self.status_message = page.locator("#opstatus")

    def open(self) -> None:
        """Navigate to the Animated Button exercise page."""
        self.page.goto("http://uitestingplayground.com/animation")

    def click_start_button(self) -> None:
        """Start the button animation."""
        self.start_button.click()

    def click_moving_target(self) -> None:
        """Wait for the target button to stop moving, then click it."""
        expect(self.target_button).to_have_class("btn btn-primary", timeout=20000)
        self.target_button.click()