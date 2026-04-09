from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TextInputPage:
    TEXT_INPUT = (By.ID, "newButtonName")
    BUTTON_PRIMARY = (By.ID, "updatingButton")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def text_input(self) -> None:
        """Clear the text input and type a new button name."""
        button_name = "Button new name"

        txt_input = self._wait().until(EC.visibility_of_element_located(self.TEXT_INPUT))
        txt_input.clear()

        txt_input.send_keys(button_name)

    def button_click(self) -> str:
        """Click the button and return its updated text."""
        primary_btn = self._wait().until(EC.element_to_be_clickable(self.BUTTON_PRIMARY))
        primary_btn.click()

        return primary_btn.text