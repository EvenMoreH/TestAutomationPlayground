from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from animated_button_selenium import AnimatedButtonPage

def test_animated_button_selenium(driver: WebDriver):
    animated_button_page = AnimatedButtonPage(driver)

    driver.get("")
