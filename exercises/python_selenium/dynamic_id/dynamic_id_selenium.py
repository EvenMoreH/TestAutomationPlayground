from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DynamicIDPage:
    BUTTON_WITH_DYNAMIC_ID = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def click_button(self) -> None:
        """Click the button that has a dynamically generated ID."""
        button = self._wait(3).until(EC.element_to_be_clickable(self.BUTTON_WITH_DYNAMIC_ID))
        button.click()