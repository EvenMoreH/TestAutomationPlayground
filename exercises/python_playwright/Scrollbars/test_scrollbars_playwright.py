from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from scrollbars_playwright import ScrollbarsPage


def test_click_hiding_button(page: Page) -> None:
    sp = ScrollbarsPage(page)
    nav = Navbar(page)

    sp.open()
    nav.page_loaded()

    sp.click_hiding_button()