from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NonBreakingSpacePage:
    BUTTON = (By.XPATH, "//button[text()='My Button']")
    BUTTON_NBSP = (By.XPATH, "//button[contains(., 'My') and contains(., 'Button')]")

    def __init__(self, driver: WebDriver) -> None:
        """Store the Selenium driver for the page object."""
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Return an explicit wait for the current driver."""
        return WebDriverWait(self.driver, timeout)

    def click_button(self) -> str:
        """
        Click the button using a fallback locator.
        For the exercise purpose, returns which locator strategy worked.
        """
        try:
            self._wait(1).until(EC.element_to_be_clickable(self.BUTTON)).click()
            return "My Button"
        except TimeoutException:
            self._wait(3).until(EC.element_to_be_clickable(self.BUTTON_NBSP)).click()
            return "My&nbsp;Button"