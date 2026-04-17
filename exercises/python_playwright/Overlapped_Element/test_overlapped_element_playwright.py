from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from overlapped_element_playwright import OverlappedElementPage

TEST_NAME = "Test-Name"

def test_input_name(page: Page) -> None:
    oep = OverlappedElementPage(page)
    nav = Navbar(page)

    oep.open()
    nav.page_loaded()

    oep.input_name(TEST_NAME)
    expect(oep.name_field).to_have_value(TEST_NAME)