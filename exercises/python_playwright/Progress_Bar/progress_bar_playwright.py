from playwright.sync_api import Page, expect


class ProgressBarPage:
    def __init__(self, page: Page):
        """Page object for the Progress Bar exercise."""
        self.page = page
        self.start_button = page.get_by_role("button", name="Start")
        self.stop_button = page.get_by_role("button", name="Stop")
        self.progress_bar = page.locator("#progressBar")
        self.result = page.locator("#result")

    def open(self) -> None:
        """Open the Progress Bar exercise page."""
        self.page.goto("http://uitestingplayground.com/progressbar")

    def click_start(self) -> None:
        """Start the progress bar."""
        self.start_button.click()

    def click_stop(self, target: int) -> None:
        """Wait for the progress bar to reach the target, then stop it."""
        handle = self.progress_bar.element_handle()
        self.page.wait_for_function(
            "([element, target]) => Number(element.getAttribute('aria-valuenow')) >= target",
            arg=[handle, target],
            timeout=30000,
            polling=5,
        )
        self.stop_button.click()