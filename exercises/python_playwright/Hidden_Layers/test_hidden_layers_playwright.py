from playwright.sync_api import Page, TimeoutError
import pytest
from hidden_layers_playwright import HiddenLayers
from exercises.python_playwright.navbar import Navbar


def test_hidden_layers_button(page: Page) -> None:
    hidden_layers = HiddenLayers(page)
    navbar = Navbar(page)

    hidden_layers.open()
    navbar.page_loaded()

    hidden_layers.click_green_button()
    with pytest.raises(TimeoutError):
        hidden_layers.click_green_button()
