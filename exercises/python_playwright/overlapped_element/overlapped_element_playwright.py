from playwright.sync_api import Page


class OverlappedElementPage:
    def __init__(self, page: Page):
        """Page object for the Overlapped Element exercise."""
        self.page = page
        self.name_field = page.get_by_placeholder("Name")

    def open(self) -> None:
        """Open the Overlapped Element exercise page."""
        self.page.goto("http://uitestingplayground.com/overlapped")

    def input_name(self, text: str) -> None:
        """Scroll the name field into view and fill it."""
        field = self.name_field
        field.hover()
        field.evaluate("element => element.scrollTop += 100")
        field.fill(text)
