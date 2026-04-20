from playwright.sync_api import Page
import pytest
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.visibility.visibility_playwright import VisibilityPage


@pytest.fixture()
def visibility_page(page: Page) -> VisibilityPage:
    vp = VisibilityPage(page)
    nav = Navbar(page)

    vp.open()
    nav.page_loaded()

    return vp

@pytest.mark.parametrize(
        "button_label",
        [
            "removed_button",
            "zero_width_button",
            "overlapped_button",
            "zero_opacity_button",
            "hidden_button",
            "none_button",
            "offscreen_button",
        ]
)
def test_button_invisible_to_user(visibility_page: VisibilityPage, button_label: str) -> None:
    visibility_page.click_hide_button()
    button = getattr(visibility_page, button_label)
    invisible, reason = visibility_page.is_invisible_for_user(button)
    assert invisible is True, reason