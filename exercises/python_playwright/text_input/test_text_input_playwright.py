import pytest
from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.text_input.text_input_playwright import TextInputPage


@pytest.mark.parametrize(
        "button_label",
        [
            "My Button",
            "My-Button",
            "theButton",
            "123",
        ]
)
def test_change_button_name_and_click(page: Page, button_label: str) -> None:
    tip = TextInputPage(page)
    nav = Navbar(page)

    tip.open()
    nav.page_loaded()

    tip.change_button_name(button_label)
    tip.click_button_by_label(button_label)