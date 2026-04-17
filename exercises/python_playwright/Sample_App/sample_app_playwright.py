from playwright.sync_api import Page


class SampleAppPage:
    def __init__(self, page: Page):
        """Page object for the Sample App exercise."""
        self.page = page
        self.login_button = page.get_by_role("button", name="Log In")
        self.username_field = page.get_by_placeholder("User Name")
        self.password_field = page.locator("[name='Password']")
        self.login_status = page.locator("#loginstatus")
        self.log_out_button = page.get_by_role("button", name="Log Out")

    def open(self) -> None:
        """Open the Sample App exercise page."""
        self.page.goto("http://uitestingplayground.com/sampleapp")

    def login(self, username: str, password: str) -> None:
        """Log in with the given username and password."""
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def log_out(self) -> None:
        """Log out of the sample app."""
        self.log_out_button.click()