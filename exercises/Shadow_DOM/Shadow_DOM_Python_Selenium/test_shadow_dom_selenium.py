from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from shadow_dom_selenium import ShadowDomPage

def test_shadow_dom_selenium(driver: WebDriver):
    shadow_dom_page = ShadowDomPage(driver)

    driver.get("")
