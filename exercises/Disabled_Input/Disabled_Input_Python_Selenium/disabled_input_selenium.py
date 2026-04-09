from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class DisabledInputPage:
    INPUT_FIELD = (By.ID, "inputField")
    BUTTON = (By.ID, "enableButton")
    STATUS_FIELD = (By.ID, "opstatus")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        """Return a WebDriverWait instance with the given timeout."""
        return WebDriverWait(self.driver, timeout)

    def _wait_until_enabled(self, field: WebElement) -> None:
        """Wait until the given field is enabled."""
        self._wait(10).until(lambda _: field.is_enabled())

    def get_status(self) -> str:
        """Return the current text of the status field."""
        status_msg = self._wait().until(EC.visibility_of_element_located(self.STATUS_FIELD))
        return status_msg.text

    def status_matches_input(self, text: str) -> bool:
        """Return True when the input field value matches the given text."""
        return self._wait().until(EC.text_to_be_present_in_element_value(self.INPUT_FIELD, text))

    def click_enable_button(self) -> None:
        """Click the button that enables the input field."""
        btn = self._wait().until(EC.element_to_be_clickable(self.BUTTON))
        btn.click()

    def input_text(self, text: str) -> None:
        """Waits for the input field to be enabled and types the given text, then confirms with Enter."""
        input_fld = self._wait().until(EC.presence_of_element_located(self.INPUT_FIELD))
        self._wait_until_enabled(input_fld)
        input_fld.clear()
        input_fld.send_keys(text)
        input_fld.send_keys(Keys.ENTER)