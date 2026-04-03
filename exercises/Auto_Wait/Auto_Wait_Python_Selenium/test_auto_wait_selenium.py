from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from auto_wait_selenium import AutoWaitPage

def test_auto_wait_selenium(driver: WebDriver):
    auto_wait_page = AutoWaitPage(driver)

    driver.get("")
