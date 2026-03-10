from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClickPage:
    BUTTON_PRIMARY = (By.CLASS_NAME, "btn-primary")
    BUTTON_SUCCESS = (By.CLASS_NAME, "btn-success")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def click_btn_primary(self):
        primary_btn = self._wait().until(EC.element_to_be_clickable(self.BUTTON_PRIMARY))
        primary_btn.click()

    def find_btn_success(self):
        if self._wait().until(EC.visibility_of_element_located(self.BUTTON_SUCCESS)):
            return True
        else:
            return False
