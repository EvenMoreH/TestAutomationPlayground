from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from click_selenium import ClickPage

def test_click_selenium(driver: WebDriver):
    click_page = ClickPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/click")
    assert page.is_loaded()
    click_page.click_btn_primary()
    result = click_page.find_btn_success()

    assert result == True