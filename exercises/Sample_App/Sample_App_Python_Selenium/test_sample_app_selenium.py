from selenium.webdriver.remote.webdriver import WebDriver
from sample_app_selenium import SampleAppPage

def test_sample_app_selenium(driver: WebDriver):
    sample_app_page = SampleAppPage(driver)

    driver.get("")
