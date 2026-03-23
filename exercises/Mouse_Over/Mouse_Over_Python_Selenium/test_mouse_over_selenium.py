from selenium.webdriver.remote.webdriver import WebDriver
from mouse_over_selenium import MouseOverPage

def test_mouse_over_selenium(driver: WebDriver):
    mouse_over_page = MouseOverPage(driver)

    driver.get("")
