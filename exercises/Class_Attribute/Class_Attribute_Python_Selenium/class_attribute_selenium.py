from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClassAttributePage:
    BUTTON_PRIMARY = (By.CLASS_NAME, "btn-primary")
    BUTTON_PRIMARY_CSS = (By.CSS_SELECTOR, "[class*='primary']")
    BUTTON_PRIMARY_XPATH = (By.XPATH, "//*[contains(@class, 'primary')]")
    BUTTON_WARNING = ""
    BUTTON_SUCCESS = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_button_primary(self):
        button_primary = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.BUTTON_PRIMARY))
        button_primary.click()

    def accept_alert(self) -> str:
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        print(f"Alert message: '{text}'")