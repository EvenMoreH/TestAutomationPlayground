import re
from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.progress_bar.progress_bar_playwright import ProgressBarPage


def test_start_stop_based_on_progress_bar(page: Page) -> None:
    pbp = ProgressBarPage(page)
    nav = Navbar(page)

    pbp.open()
    nav.page_loaded()

    pbp.click_start()
    pbp.click_stop(75)
    expect(pbp.result).to_have_text(re.compile("Result: 0"))