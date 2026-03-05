from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DynamicIDPage:
    BUTTON_WITH_DYNAMIC_ID = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def click_button(self):
        button = self._wait(3).until(EC.element_to_be_clickable(self.BUTTON_WITH_DYNAMIC_ID))
        button.click()