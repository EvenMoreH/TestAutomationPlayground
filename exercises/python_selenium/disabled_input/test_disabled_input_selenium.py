from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.disabled_input.disabled_input_selenium import (
    DisabledInputPage,
)

TEST_TEXT = "test-value"

def test_disabled_input_selenium(driver: WebDriver):
    disabled_input_page = DisabledInputPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/disabledinput")
    assert page.is_loaded()
    assert disabled_input_page.get_status() == "---"

    disabled_input_page.click_enable_button()
    disabled_input_page.input_text(TEST_TEXT)

    assert disabled_input_page.status_matches_input(TEST_TEXT)