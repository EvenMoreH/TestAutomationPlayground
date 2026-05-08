from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.verify_text.verify_text_playwright import VerifyTextPage


def test_find_welcome_message(page: Page) -> None:
    vtp = VerifyTextPage(page)
    nav = Navbar(page)

    vtp.open()
    nav.page_loaded()

    message = "Welcome UserName!"
    expect(vtp.welcome_msg).to_have_text(message, use_inner_text=True)