from playwright.sync_api import FrameLocator, Page


class FramesPage:
    def __init__(self, page: Page):
        """Initialize page, frame locators, and result locators."""
        self.page = page
        self.outer_frame = page.frame_locator("#frame-outer")
        self.outer_result = self.outer_frame.locator("#result")
        self.inner_frame = self.outer_frame.frame_locator("#frame-inner")
        self.inner_result = self.inner_frame.locator("#result")

    def open(self) -> None:
        """Open the frames exercise page."""
        self.page.goto("http://uitestingplayground.com/frames")

    def click_edit_button_in_frame(self, frame: FrameLocator) -> None:
        """Click the Edit button inside the given frame."""
        edit_button = frame.locator("[data-action='edit']")
        edit_button.click()

    def click_submit_button_in_frame(self, frame: FrameLocator) -> None:
        """Click the Submit button inside the given frame."""
        submit_button = frame.get_by_text("Submit")
        submit_button.click()

    def click_click_me_button_in_frame(self, frame: FrameLocator) -> None:
        """Click the Click me button inside the given frame."""
        click_me_button = frame.locator("button[name='my-button']")
        click_me_button.click()

    def click_primary_button_in_frame(self, frame: FrameLocator) -> None:
        """Click the Primary button inside the given frame."""
        primary_button = frame.locator(".btn-class")
        primary_button.click()
