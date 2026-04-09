from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

Locator = tuple[str, str]

class AlertsPage:
    ALERT_BUTTON = (By.ID, "alertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promptButton")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def _click(self, locator: Locator) -> None:
        self._wait().until(EC.element_to_be_clickable(locator)).click()

    def _access_alert(self) -> Alert:
        return self._wait().until(EC.alert_is_present())

    def trigger_alert(self) -> None:
        self._click(self.ALERT_BUTTON)

    def trigger_confirm(self) -> None:
        self._click(self.CONFIRM_BUTTON)

    def trigger_prompt(self) -> None:
        self._click(self.PROMPT_BUTTON)

    def is_alert_closed(self) -> bool:
        try:
            self._wait().until_not(EC.alert_is_present())
            return True
        except Exception:
            return False

    def confirm_alert(self) -> None:
        alert = self._access_alert()
        alert.accept()

