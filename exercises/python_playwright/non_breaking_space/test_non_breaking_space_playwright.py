from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.non_breaking_space.non_breaking_space_playwright import NBSPPage


def test_click_nbsp_button(page: Page) -> None:
    nav = Navbar(page)
    nbspp = NBSPPage(page)

    nbspp.open()
    nav.page_loaded()

    nbspp.click_button()