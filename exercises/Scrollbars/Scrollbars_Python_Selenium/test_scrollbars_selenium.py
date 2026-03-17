from selenium.webdriver.remote.webdriver import WebDriver
from scrollbars_selenium import ScrollbarsPage

def test_click_hidden_btn(driver: WebDriver):
    scrollbars_page = ScrollbarsPage(driver)

    driver.get("http://uitestingplayground.com/scrollbars")

    scrollbars_page.click_button()