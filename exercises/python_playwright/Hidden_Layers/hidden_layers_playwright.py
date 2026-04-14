from playwright.sync_api import Page


class HiddenLayers:
    def __init__(self, page: Page):
        """Store the Playwright page and element locators."""
        self.page = page
        self.green_button = page.locator("#greenButton")


    def open(self) -> None:
        """Open the Hidden Layers exercise page."""
        self.page.goto("http://uitestingplayground.com/hiddenlayers")


    def click_green_button(self) -> None:
        """Click the green button."""
        self.green_button.click(timeout=3000)