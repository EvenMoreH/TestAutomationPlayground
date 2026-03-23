from selenium.webdriver.remote.webdriver import WebDriver
from frames_selenium import FramesPage

def test_frames_selenium(driver: WebDriver):
    frames_page = FramesPage(driver)

    driver.get("")
