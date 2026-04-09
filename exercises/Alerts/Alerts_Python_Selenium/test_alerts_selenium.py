from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from alerts_selenium import AlertsPage

def test_alert_btn_selenium(driver: WebDriver):
    alerts_page = AlertsPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/alerts")
    assert page.is_loaded()

    alerts_page.trigger_alert()
    alerts_page.confirm_alert()
    assert alerts_page.is_alert_closed() == True