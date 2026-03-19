from selenium.webdriver.remote.webdriver import WebDriver
from verify_text import VerifyTextPage

def test_verify_text(driver: WebDriver):
    verify_text_page = VerifyTextPage(driver)

    driver.get("http://uitestingplayground.com/verifytext")
    text = verify_text_page.capture_text()

    assert text == "Welcome UserName!"