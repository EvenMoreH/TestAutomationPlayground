from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from frames_selenium import FramesPage

def test_frames_selenium(driver: WebDriver):
    frames_page = FramesPage(driver)

    driver.get("")
