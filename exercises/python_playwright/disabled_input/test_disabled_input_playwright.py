from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.disabled_input.disabled_input_playwright import DisabledInput


TEST_TEXT = "test-input"

def test_wait_for_enabled_input(page: Page) -> None:
    disabled_input = DisabledInput(page)
    navbar = Navbar(page)

    disabled_input.open()
    navbar.page_loaded()

    disabled_input.click_enable_edit_button()
    disabled_input.input_text(TEST_TEXT)
    expect(disabled_input.status_field).to_contain_text(TEST_TEXT)