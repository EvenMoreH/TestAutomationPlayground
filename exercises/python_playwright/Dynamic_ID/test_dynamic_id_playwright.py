from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from dynamic_id_playwright import DynamicID


def test_dynamic_id_button(page: Page) -> None:
    dynamic_id_page = DynamicID(page)
    navbar = Navbar(page)

    dynamic_id_page.open()
    navbar.page_loaded()

    dynamic_id_page.click_dynamic_button()