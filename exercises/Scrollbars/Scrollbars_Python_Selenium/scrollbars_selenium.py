from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ScrollbarsPage:
    PRIMARY_BUTTON = (By.ID, "hidingButton")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def _scroll_to_button(self) -> WebElement:
        """Scroll the hidden button into view and return it."""
        button = self._wait().until(EC.presence_of_element_located(self.PRIMARY_BUTTON))

        ActionChains(self.driver).move_to_element(button).perform()
        return button

    def click_button(self) -> None:
        """Scroll to the hidden button and click it."""
        hidden_button = self._scroll_to_button()
        hidden_button.click()