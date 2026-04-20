from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.animated_button.animated_button_selenium import (
    AnimatedButtonPage,
)

def test_animated_button_selenium(driver: WebDriver):
    animated_button_page = AnimatedButtonPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/animation")
    assert page.is_loaded()
    assert animated_button_page.get_status() == "---"

    animated_button_page.click_start_button()
    assert animated_button_page.get_status() == "Animating the button..."

    animated_button_page.click_moving_button()
    assert "spin" not in animated_button_page.get_status()