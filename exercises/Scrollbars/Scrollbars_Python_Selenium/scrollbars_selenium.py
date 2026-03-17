from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ScrollbarsPage:
    PRIMARY_BUTTON = (By.ID, "hidingButton")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def _scroll_to_button(self):
        button = self._wait().until(EC.presence_of_element_located(self.PRIMARY_BUTTON))

        ActionChains(self.driver).move_to_element(button).perform()
        return button

    def click_button(self):
        hidden_button = self._scroll_to_button()
        hidden_button.click()