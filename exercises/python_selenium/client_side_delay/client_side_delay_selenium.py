from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientSideDelay:
    AJAX_BUTTON = (By.ID, "ajaxButton")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "bg-success")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def click_ajax_button(self) -> None:
        """Click the button that triggers client-side processing."""
        ajax_btn = self._wait().until(EC.element_to_be_clickable(self.AJAX_BUTTON))
        ajax_btn.click()

    def get_success_message(self) -> str:
        """Return the text of the success message after processing completes."""
        success_msg = self._wait(20).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return success_msg.text