from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HiddenLayersPage:
    GREEN_BUTTON = (By.ID, "greenButton")
    BLUE_BUTTON = (By.ID, "blueButton")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def click_button_green(self) -> None:
        """Click the green button."""
        button_g = self._wait(3).until(EC.element_to_be_clickable(self.GREEN_BUTTON))
        button_g.click()

    def click_button_blue(self) -> None:
        """Click the blue button."""
        button_b = self._wait(3).until(EC.element_to_be_clickable(self.BLUE_BUTTON))
        button_b.click()
