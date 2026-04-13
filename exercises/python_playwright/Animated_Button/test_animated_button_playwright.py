from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from animated_button_playwright import AnimatedButton


BUTTON_CLICK_RESULT = "Moving Target clicked. It's class name is 'btn btn-primary'"

def test_click_moving_button(page: Page) -> None:
    animated_button_page = AnimatedButton(page)
    navbar = Navbar(page)

    animated_button_page.open()
    navbar.page_loaded()

    expect (animated_button_page.status_message).to_contain_text("---")

    animated_button_page.click_start_button()
    animated_button_page.click_moving_target()

    expect (animated_button_page.status_message).to_contain_text(BUTTON_CLICK_RESULT)