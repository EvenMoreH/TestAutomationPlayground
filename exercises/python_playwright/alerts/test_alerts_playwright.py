from playwright.sync_api import Page
import pytest
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.alerts.alerts_playwright import AlertsPage


@pytest.fixture
def alerts_page(page: Page) -> AlertsPage:
    alerts_page = AlertsPage(page)
    navbar = Navbar(page)

    alerts_page.open()
    navbar.page_loaded()

    return alerts_page

def test_alert_button(alerts_page: AlertsPage) -> None:
    alerts_page.click_alert()


@pytest.mark.parametrize(
        "accept, expected",
        [
            (True, "Yes"),
            (False, "No"),
        ]
)
def test_confirm_button(alerts_page: AlertsPage, accept: bool, expected: str) -> None:
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
def test_prompt_button(alerts_page: AlertsPage, input_text: str, expected: str) -> None:
    alert_message = alerts_page.click_prompt(input_text)
    assert alert_message == "User value: " + expected