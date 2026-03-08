import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from load_delay_selenium_main_page import MainPage
from load_delay_selenium import LoadDelayPage

def test_delayed_button_click(driver: WebDriver):
    load_delay_main_page = MainPage(driver)
    load_delay_page = LoadDelayPage(driver)

    main_page_url = "uitestingplayground.com"
    load_delay_page_url = "uitestingplayground.com/loaddelay"

    load_delay_main_page.open_main_page()
    assert main_page_url in driver.current_url

    load_delay_main_page.click_category_load_delays()
    assert load_delay_page_url in driver.current_url

    load_delay_page.click_delayed_button()
