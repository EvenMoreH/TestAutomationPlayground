from selenium.webdriver.remote.webdriver import WebDriver
from text_input_selenium import TextInputPage

def test_click_selenium(driver: WebDriver):
    text_input_page = TextInputPage(driver)

    driver.get("http://uitestingplayground.com/textinput")

    text_input_page.text_input()
    new_button_name = text_input_page.button_click()

    assert new_button_name == "Button new name"