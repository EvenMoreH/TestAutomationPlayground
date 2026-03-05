from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClassAttributePage:
    BUTTON_PRIMARY = (By.CLASS_NAME, "btn-primary")
    BUTTON_WARNING = (By.CSS_SELECTOR, "[class*='success']")
    BUTTON_SUCCESS = (By.XPATH, "//*[contains(@class, 'warning')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def click_button_primary(self):
        button_primary = self._wait(3).until(EC.element_to_be_clickable(self.BUTTON_PRIMARY))
        button_primary.click()

    def click_button_warning(self):
        button_warning = self._wait(3).until(EC.element_to_be_clickable(self.BUTTON_WARNING))
        button_warning.click()

    def click_button_success(self):
        button_success = self._wait(3).until(EC.element_to_be_clickable(self.BUTTON_SUCCESS))
        button_success.click()

    def accept_alert(self) -> str:
        alert = self._wait(3).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text