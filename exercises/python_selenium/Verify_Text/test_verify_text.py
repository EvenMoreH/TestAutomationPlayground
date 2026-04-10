from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from verify_text import VerifyTextPage

def test_verify_text(driver: WebDriver):
    verify_text_page = VerifyTextPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/verifytext")
    assert page.is_loaded()
    text = verify_text_page.capture_text()

    assert text == "Welcome UserName!"