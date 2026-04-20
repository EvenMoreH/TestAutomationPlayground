from playwright.sync_api import Page


class ShadowDOMPage:
    def __init__(self, page: Page):
        """Store page and locators used by the exercise."""
        self.page = page
        self.edit_field = page.locator("#editField")
        self.generate_button = page.locator("#buttonGenerate")
        self.copy_button = page.locator("#buttonCopy")

    def open(self) -> None:
        """Open the page over HTTPS despite default address being HTTP so clipboard functionality works."""
        self.page.goto("https://uitestingplayground.com/shadowdom")

    def generate_guid(self) -> str:
        """Generate a new GUID and return the input value."""
        self.generate_button.click()
        return self.edit_field.input_value()

    def copy_guid(self) -> None:
        """Copy the generated GUID to the clipboard."""
        self.copy_button.click()