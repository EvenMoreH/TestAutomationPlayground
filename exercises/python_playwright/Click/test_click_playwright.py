from playwright.sync_api import Page, expect
from click_playwright import Click
from exercises.python_playwright.navbar import Navbar


def test_hidden_layers_button(page: Page) -> None:
    click_page = Click(page)
    navbar = Navbar(page)

    click_page.open()
    navbar.page_loaded()

    click_page.click_button()
    expect(click_page.button).to_contain_class("btn-success")