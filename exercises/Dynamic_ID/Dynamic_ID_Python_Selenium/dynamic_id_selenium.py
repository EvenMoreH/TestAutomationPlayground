from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_waits import SeleniumWaits

class DynamicIDPage:
    BUTTON_WITH_DYNAMIC_ID = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.waits = SeleniumWaits(driver, default_timeout=8)

    def click_button(self, timeout: int | None = None):
        button = self.waits.clickable(self.BUTTON_WITH_DYNAMIC_ID, timeout=timeout)
        button.click()