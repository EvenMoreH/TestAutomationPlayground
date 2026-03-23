from selenium.webdriver.remote.webdriver import WebDriver
from visibility_selenium import VisibilityPage

def test_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("")
