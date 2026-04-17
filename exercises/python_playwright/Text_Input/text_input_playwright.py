from playwright.sync_api import Page


class TextInputPage:
    def __init__(self, page: Page):
        """Store page and locators used by the exercise."""
        self.page = page
        self.input_field = page.get_by_placeholder("MyButton")
        self.default_button = page.locator("#updatingButton")

    def open(self) -> None:
        """Open the Text Input exercise page."""
        self.page.goto("http://uitestingplayground.com/textinput")

    def change_button_name(self, text: str) -> None:
        """Update the button label with given text through the input field and submit it."""
        self.input_field.clear()
        self.input_field.fill(text)
        self.default_button.click()

    def click_button_by_label(self, button_label: str) -> None:
        """Click the button using its current visible label."""
        self.page.get_by_role("button", name=button_label).click()