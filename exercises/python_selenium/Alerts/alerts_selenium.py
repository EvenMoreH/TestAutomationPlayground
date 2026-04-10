"""Page object for the Alerts Selenium exercise."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

Locator = tuple[str, str]


class AlertsPage:
    """Encapsulates interactions with the alerts exercise page."""

    ALERT_BUTTON = (By.ID, "alertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promptButton")

    def __init__(self, driver: WebDriver) -> None:
        """Store the browser driver used to interact with the page."""
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def _click(self, locator: Locator) -> None:
        """Wait for an element to be clickable, then click it."""
        self._wait().until(EC.element_to_be_clickable(locator)).click()

    def _access_alert(self) -> Alert:
        """Wait for a browser alert to appear and return it."""
        return self._wait().until(EC.alert_is_present())

    def _clear_prompt_field(self) -> None:
        """
        Select all text in the prompt field and delete it.
        Workaround due to .clear() being not available for alert prompts.
        """
        alert = self._access_alert()
        alert.send_keys(Keys.CONTROL + "a")
        alert.send_keys(Keys.BACKSPACE)

    def trigger_alert(self) -> None:
        """Click the button that triggers a simple alert."""
        self._click(self.ALERT_BUTTON)

    def trigger_confirmation(self) -> None:
        """Click the button that triggers a confirmation dialog."""
        self._click(self.CONFIRM_BUTTON)

    def trigger_prompt(self) -> None:
        """Click the button that triggers a prompt dialog."""
        self._click(self.PROMPT_BUTTON)

    def is_alert_closed(self) -> bool:
        """Return True if no alert is currently present."""
        try:
            self._wait().until_not(EC.alert_is_present())
            return True
        except Exception:
            return False

    def confirm_alert(self) -> None:
        """Accept the currently active alert."""
        alert = self._access_alert()
        alert.accept()

    def dismiss_alert(self) -> None:
        """Dismiss the currently active alert."""
        alert = self._access_alert()
        alert.dismiss()

    def input_prompt(self, text: str) -> None:
        """Clear the prompt field, type the given text, and accept."""
        self._clear_prompt_field()
        alert = self._access_alert()
        alert.send_keys(text)
        alert.accept()

    def get_prompt_text(self) -> str:
        """Return the text displayed in the currently active alert."""
        alert = self._access_alert()
        return alert.text
