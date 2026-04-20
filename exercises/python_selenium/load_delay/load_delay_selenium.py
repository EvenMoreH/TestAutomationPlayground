from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoadDelayPage:
    LOAD_DELAY_LINK = (By.LINK_TEXT, "Load Delay")
    DELAYED_BUTTON = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def click_delayed_button(self) -> None:
        """Wait for and click the button that appears after a load delay."""
        delayed_btn = self._wait(10).until(EC.element_to_be_clickable(self.DELAYED_BUTTON))
        delayed_btn.click()