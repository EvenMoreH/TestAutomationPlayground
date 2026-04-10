from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    LOAD_DELAY_LINK = (By.LINK_TEXT, "Load Delay")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def open_main_page(self):
        self.driver.get("http://uitestingplayground.com")

    def click_category_load_delays(self):
        category_link = self._wait(5).until(EC.element_to_be_clickable(self.LOAD_DELAY_LINK))
        category_link.click()