from playwright.sync_api import Page, expect
import pytest
from exercises.python_playwright.navbar import Navbar
from mouse_over_playwright import MouseOverPage

@pytest.fixture
def mouse_over_page(page: Page) -> MouseOverPage:
    mop = MouseOverPage(page)
    nav = Navbar(page)

    mop.open()
    nav.page_loaded()

    return mop

def test_double_click_click_me_btn(mouse_over_page: MouseOverPage) -> None:
    mouse_over_page.doubleclick_button_click_me()
    expect(mouse_over_page.click_me_click_count).to_contain_text("2")

def test_double_click_link_btn(mouse_over_page: MouseOverPage) -> None:
    mouse_over_page.doubleclick_button_link_button()
    expect(mouse_over_page.link_btn_click_count).to_contain_text("2")