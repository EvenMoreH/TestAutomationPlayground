from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from sample_app_selenium import SampleAppPage

def test_sample_app_selenium(driver: WebDriver):
    sample_app_page = SampleAppPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/sampleapp")
    assert page.is_loaded()
