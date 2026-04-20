from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.ajax_data.ajax_data_playwright import AjaxData

SUCCESS_MSG = "Data loaded with AJAX get request."

def test_ajax_data(page: Page) -> None:
    ajax_page = AjaxData(page)
    navbar = Navbar(page)

    ajax_page.open()
    navbar.page_loaded()

    ajax_page.click_ajax_button()
    expect(ajax_page.ajax_status).to_have_text(SUCCESS_MSG, timeout=25000)