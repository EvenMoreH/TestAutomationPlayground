from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VerifyTextPage:
    WELCOME_TEXT = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def capture_text(self) -> str:
        """Return the welcome text from the page."""
        result = self._wait().until(EC.presence_of_element_located(self.WELCOME_TEXT))
        return result.text.strip()