from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from dynamic_table_playwright import DynamicTable


def test_compare_chrome_usage(page: Page) -> None:
    dynamic_table_page = DynamicTable(page)
    navbar = Navbar(page)

    dynamic_table_page.open()
    navbar.page_loaded()

    table_value = dynamic_table_page.get_cell_value("CPU", "Chrome")
    banner_value = dynamic_table_page.get_banner_value()

    assert banner_value == f"Chrome CPU: {table_value}"
