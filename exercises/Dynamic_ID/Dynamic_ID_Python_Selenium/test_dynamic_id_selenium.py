import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from dynamic_id_selenium import DynamicIDPage

def test_dynamic_id_selenium(driver: WebDriver):
    dynamic_id_page = DynamicIDPage(driver)

    driver.get("http://uitestingplayground.com/dynamicid")

    dynamic_id_page.click_button()