from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage

from class_attribute_selenium import ClassAttributePage

def test_primary_button_class_attribute_selenium(driver: WebDriver):
    class_attribute_page = ClassAttributePage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/classattr")
    assert page.is_loaded()

    class_attribute_page.click_button_primary()
    alert_text = class_attribute_page.accept_alert()
    assert alert_text == "Primary button pressed"

def test_warning_button_class_attribute_selenium(driver: WebDriver):
    class_attribute_page = ClassAttributePage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/classattr")
    assert page.is_loaded()

    class_attribute_page.click_button_warning()

def test_success_button_class_attribute_selenium(driver: WebDriver):
    class_attribute_page = ClassAttributePage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/classattr")
    assert page.is_loaded()

    class_attribute_page.click_button_success()
