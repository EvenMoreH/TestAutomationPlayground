from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from non_breaking_space_selenium import NonBreakingSpacePage

def test_non_breaking_space_selenium(driver: WebDriver):
    non_breaking_space_page = NonBreakingSpacePage(driver)

    driver.get("")
