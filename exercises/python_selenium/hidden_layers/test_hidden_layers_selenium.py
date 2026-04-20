import pytest
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.hidden_layers.hidden_layers_selenium import (
    HiddenLayersPage,
)

def test_hidden_layers_green_btn(driver: WebDriver):
    """Verify the exercise behavior that the green button cannot be clicked twice.

    The first click activates the overlapping blue layer. A second attempt to
    click the original green button should be intercepted because that button is
    no longer the top clickable element from the user's perspective.
    """
    hidden_layers_page = HiddenLayersPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/hiddenlayers")
    assert page.is_loaded()
    hidden_layers_page.click_button_green()
    with pytest.raises(ElementClickInterceptedException):
        hidden_layers_page.click_button_green()

def test_hidden_layers_green_and_blue_btn(driver: WebDriver):
    """Demonstrate the correct interaction after the overlap changes.

    Once the green button is clicked, the blue button becomes the visible and
    clickable layer on top. This test shows the proper follow-up action when
    working with overlapping elements instead of retrying the hidden button.
    """
    hidden_layers_page = HiddenLayersPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/hiddenlayers")
    assert page.is_loaded()
    hidden_layers_page.click_button_green()
    hidden_layers_page.click_button_blue()