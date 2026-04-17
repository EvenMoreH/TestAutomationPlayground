from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from verify_text_playwright import VerifyTextPage


def test_find_welcome_message(page: Page) -> None:
    vtp = VerifyTextPage(page)
    nav = Navbar(page)

    vtp.open()
    nav.page_loaded()

    message = vtp.find_and_return_welcome_message()
    assert message == "Welcome UserName!"