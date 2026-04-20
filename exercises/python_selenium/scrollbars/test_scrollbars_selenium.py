from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.scrollbars.scrollbars_selenium import ScrollbarsPage

def test_click_hidden_btn(driver: WebDriver):
    scrollbars_page = ScrollbarsPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/scrollbars")
    assert page.is_loaded()

    scrollbars_page.click_button()