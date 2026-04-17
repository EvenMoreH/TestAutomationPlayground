from playwright.sync_api import Page, expect
import pytest
from exercises.python_playwright.navbar import Navbar
from sample_app_playwright import SampleAppPage


@pytest.fixture
def sample_app_page(page: Page) -> SampleAppPage:
    sap = SampleAppPage(page)
    nav = Navbar(page)

    sap.open()
    nav.page_loaded()
    expect(sap.login_status).to_have_text("User logged out.")

    return sap


@pytest.mark.parametrize(
        "username, password, expected",
        [
            ("test-user", "pwd", "Welcome, test-user!"),
            ("New-user", "pwd", "Welcome, New-user!"),
            ("James", "pwd", "Welcome, James!"),
        ]
)
def test_log_in(sample_app_page: SampleAppPage, username: str, password: str, expected: str) -> None:
    sample_app_page.login(username, password)
    expect(sample_app_page.login_status).to_have_text(expected)


@pytest.mark.parametrize(
        "username, password",
        [
            ("User", "pwd"),
            ("NewUser", "pwd"),
            ("James", "pwd"),
        ]
)
def test_log_out(sample_app_page: SampleAppPage, username: str, password: str) -> None:
    sample_app_page.login(username, password)
    expect(sample_app_page.login_status).to_have_text(f"Welcome, {username}!")

    sample_app_page.log_out()
    expect(sample_app_page.login_status).to_have_text("User logged out.")


@pytest.mark.parametrize(
        "username, password",
        [
            ("User", "test_password"),
            ("NewUser", ""),
            ("James", "1234"),
        ]
)
def test_bad_login(sample_app_page: SampleAppPage, username: str, password: str) -> None:
    sample_app_page.login(username, password)
    expect(sample_app_page.login_status).to_have_text("Invalid username/password")