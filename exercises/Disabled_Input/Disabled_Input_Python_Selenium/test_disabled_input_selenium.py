from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from disabled_input_selenium import DisabledInputPage

def test_disabled_input_selenium(driver: WebDriver):
    disabled_input_page = DisabledInputPage(driver)

    driver.get("")
