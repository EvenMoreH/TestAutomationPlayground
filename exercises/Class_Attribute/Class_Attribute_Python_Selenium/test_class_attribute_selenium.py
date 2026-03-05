import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from class_attribute_selenium import ClassAttributePage

def test_class_attribute_selenium(driver: WebDriver):
    class_attribute_page = ClassAttributePage(driver)

    driver.get("http://uitestingplayground.com/classattr")

    class_attribute_page.click_button_primary()
    class_attribute_page.accept_alert()