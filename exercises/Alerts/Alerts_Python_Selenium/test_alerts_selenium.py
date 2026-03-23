from selenium.webdriver.remote.webdriver import WebDriver
from alerts_selenium import AlertsPage

def test_alerts_selenium(driver: WebDriver):
    alerts_page = AlertsPage(driver)

    driver.get("")
