import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from alerts_selenium import AlertsPage

URL = "http://uitestingplayground.com/alerts"

def test_alert_btn_selenium(driver: WebDriver):
    alerts_page = AlertsPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    alerts_page.trigger_alert()
    alerts_page.confirm_alert()
    assert alerts_page.is_alert_closed() == True

def test_confirm_btn_accept_selenium(driver: WebDriver):
    alerts_page = AlertsPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    alerts_page.trigger_confirmation()
    alerts_page.confirm_alert()
    alerts_page.confirm_alert()
    assert alerts_page.is_alert_closed() == True

def test_confirm_btn_reject_selenium(driver: WebDriver):
    alerts_page = AlertsPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    alerts_page.trigger_confirmation()
    alerts_page.dismiss_alert()
    alerts_page.confirm_alert()
    assert alerts_page.is_alert_closed() == True

@pytest.mark.parametrize("test_prompt", [
    "cats",
    "dogs",
    "test-value",
    "",
])
def test_prompt_btn_selenium(driver: WebDriver, test_prompt):
    alerts_page = AlertsPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    alerts_page.trigger_prompt()
    alerts_page.input_prompt(test_prompt)
    assert alerts_page.get_prompt_text() == f"User value: {test_prompt}"

    alerts_page.confirm_alert()
    assert alerts_page.is_alert_closed() == True