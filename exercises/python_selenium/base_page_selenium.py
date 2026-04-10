from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException

class BasePage:
    PAGE_READY_LOCATOR = (By.CLASS_NAME, "navbar-brand")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def is_loaded(self):
        try:
            self._wait().until(EC.visibility_of_element_located(self.PAGE_READY_LOCATOR))
            return True
        except TimeoutException:
            return False