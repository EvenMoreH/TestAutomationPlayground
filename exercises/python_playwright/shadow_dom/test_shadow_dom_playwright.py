import pytest
from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.shadow_dom.shadow_dom_playwright import ShadowDOMPage


@pytest.fixture
def context(browser):
    return browser.new_context(
        ignore_https_errors=True,
        permissions=["clipboard-read", "clipboard-write"]
    )

def test_generate_and_copy_guid(page: Page) -> None:
    sdp = ShadowDOMPage(page)
    nav = Navbar(page)

    sdp.open()
    nav.page_loaded()

    generated_guid = sdp.generate_guid()
    sdp.copy_guid()
    copied_guid_value = page.evaluate("navigator.clipboard.readText()")

    assert generated_guid == copied_guid_value