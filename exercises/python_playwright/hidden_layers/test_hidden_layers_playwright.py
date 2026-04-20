from playwright.sync_api import Page, TimeoutError
import pytest
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.hidden_layers.hidden_layers_playwright import HiddenLayers


def test_hidden_layers_button(page: Page) -> None:
    hidden_layers = HiddenLayers(page)
    navbar = Navbar(page)

    hidden_layers.open()
    navbar.page_loaded()

    hidden_layers.click_green_button()
    with pytest.raises(TimeoutError):
        hidden_layers.click_green_button()
