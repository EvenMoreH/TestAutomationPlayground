from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.client_side_delay.client_side_delay_playwright import ClientSideDelay


SUCCESS_MESSAGE = "Data calculated on the client side."

def test_client_side_delay(page: Page) -> None:
    csd_page = ClientSideDelay(page)
    navbar = Navbar(page)

    csd_page.open()
    navbar.page_loaded()

    expect(csd_page.success_label).not_to_be_visible()

    csd_page.trigger_client_logic()

    expect(csd_page.success_label).to_contain_text(SUCCESS_MESSAGE, timeout=20000)