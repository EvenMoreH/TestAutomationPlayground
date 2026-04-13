from playwright.sync_api import Page
import pytest
from exercises.python_playwright.navbar import Navbar
from alerts_playwright import AlertsPage


def test_alert_button(page: Page) -> None:
    alerts_page = AlertsPage(page)
    navbar = Navbar(page)

    alerts_page.open()
    navbar.page_loaded()

    alerts_page.click_alert()


@pytest.mark.parametrize(
        "accept, expected",
        [
            (True, "Yes"),
            (False, "No"),
        ]
)
def test_confirm_button(page: Page, accept: bool, expected: str) -> None:
    alerts_page = AlertsPage(page)
    navbar = Navbar(page)

    alerts_page.open()
    navbar.page_loaded()

    alert_message = alerts_page.click_confirm(accept)
    assert alert_message == expected


@pytest.mark.parametrize(
        "input_text, expected",
        [
            ("Cats", "Cats"),
            ("Dogs", "Dogs"),
            ("Fish", "Fish"),
            ("", ""),
            (" ", " "),
        ]
)
def test_prompt_button(page: Page, input_text: str, expected: str) -> None:
    alerts_page = AlertsPage(page)
    navbar = Navbar(page)

    alerts_page.open()
    navbar.page_loaded()

    alert_message = alerts_page.click_prompt(input_text)
    assert alert_message == "User value: " + expected