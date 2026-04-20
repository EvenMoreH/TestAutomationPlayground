from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.dynamic_id.dynamic_id_selenium import DynamicIDPage

def test_dynamic_id_selenium(driver: WebDriver):
    dynamic_id_page = DynamicIDPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/dynamicid")
    assert page.is_loaded()

    dynamic_id_page.click_button()