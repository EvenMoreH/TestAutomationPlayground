from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SampleAppPage:
    STATUS_ELEMENT = (By.ID, "loginstatus")
    USER_NAME_FIELD = (By.NAME, "UserName")
    PASSWORD_FIELD = (By.NAME, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log In']")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Log Out']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)
