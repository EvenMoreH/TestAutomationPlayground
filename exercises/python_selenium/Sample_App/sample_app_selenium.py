from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SampleAppPage:
    STATUS_ELEMENT = (By.ID, "loginstatus")
    USER_NAME_FIELD = (By.NAME, "UserName")
    PASSWORD_FIELD = (By.NAME, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log In']")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Log Out']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def _input_credentials(self, user_name: str, password: str) -> None:
        """Clear and fill the username and password fields."""
        user_name_input = self._wait().until(EC.visibility_of_element_located(self.USER_NAME_FIELD))
        user_name_input.clear()
        user_name_input.send_keys(user_name)

        password_input = self._wait().until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        password_input.clear()
        password_input.send_keys(password)

    def _click_login_button(self) -> None:
        """Click the login button."""
        self._wait().until(EC.visibility_of_element_located(self.LOGIN_BUTTON)).click()

    def login_as_test_user(self, user_name: str, password: str) -> None:
        """Fill credentials and submit the login form."""
        self._input_credentials(user_name, password)
        self._click_login_button()

    def click_logout_button(self) -> None:
        """Click the logout button."""
        self._wait().until(EC.visibility_of_element_located(self.LOGOUT_BUTTON)).click()

    def login_status(self) -> str:
        """Return the current login status text."""
        return self._wait().until(EC.visibility_of_element_located(self.STATUS_ELEMENT)).text.strip()
