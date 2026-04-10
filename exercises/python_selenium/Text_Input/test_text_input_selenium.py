from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from text_input_selenium import TextInputPage

def test_click_selenium(driver: WebDriver):
    text_input_page = TextInputPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/textinput")
    assert page.is_loaded()

    text_input_page.text_input()
    new_button_name = text_input_page.button_click()

    assert new_button_name == "Button new name"