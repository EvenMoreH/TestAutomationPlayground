from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.sample_app.sample_app_selenium import SampleAppPage

USER_NAME = "test-user"
PASSWORD = "pwd"
URL = "http://uitestingplayground.com/sampleapp"

def test_login_sample_app_selenium(driver: WebDriver):
    sample_app_page = SampleAppPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    status = sample_app_page.login_status()
    assert status == "User logged out."

    sample_app_page.login_as_test_user(USER_NAME, PASSWORD)

    status = sample_app_page.login_status()
    assert status == f"Welcome, {USER_NAME}!"

def test_bad_password_login_sample_app_selenium(driver: WebDriver):
    sample_app_page = SampleAppPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    status = sample_app_page.login_status()
    assert status == "User logged out."

    sample_app_page.login_as_test_user(USER_NAME, "test-password")

    status = sample_app_page.login_status()
    assert status == "Invalid username/password"

def test_empty_username_login_sample_app_selenium(driver: WebDriver):
    sample_app_page = SampleAppPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    status = sample_app_page.login_status()
    assert status == "User logged out."

    sample_app_page.login_as_test_user("", PASSWORD)

    status = sample_app_page.login_status()
    assert status == "Invalid username/password"


def test_logout_sample_app_selenium(driver: WebDriver):
    sample_app_page = SampleAppPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    sample_app_page.login_as_test_user(USER_NAME, PASSWORD)
    sample_app_page.click_logout_button()

    status = sample_app_page.login_status()
    assert status == "User logged out."