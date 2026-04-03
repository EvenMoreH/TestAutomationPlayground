from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from overlapped_element_selenium import OverlappedElementPage

def test_overlapped_element_selenium(driver: WebDriver):
    overlapped_element_page = OverlappedElementPage(driver)

    driver.get("")
