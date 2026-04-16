from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from load_delay_playwright import DelayMainPage, DelayExercisePage


def test_click_button_after_redirection(page: Page) -> None:
    nav = Navbar(page)
    dmp = DelayMainPage(page)
    dep = DelayExercisePage(page)

    dmp.open()
    nav.page_loaded()

    dmp.click_link()
    expect(page).to_have_url("http://uitestingplayground.com/loaddelay")

    dep.click_button()