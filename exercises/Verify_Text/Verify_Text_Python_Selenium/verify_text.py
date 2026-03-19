from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VerifyTextPage:
    WELCOME_TEXT = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def capture_text(self) -> str:
        result = self._wait().until(EC.presence_of_element_located(self.WELCOME_TEXT))
        return result.text.strip()