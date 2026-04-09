from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FileUploadPage:
    IFRAME = (By.CSS_SELECTOR, "iframe")
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    FILE_CONTAINER = (By.CLASS_NAME, "file-info")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def _switch_to_upload_iframe(self) -> None:
        upload_iframe = self._wait().until(EC.presence_of_element_located(self.IFRAME))
        self.driver.switch_to.frame(upload_iframe)

    def upload_file(self, file_path: str) -> None:
        self._switch_to_upload_iframe()
        file_dialog = self._wait().until(EC.presence_of_element_located(self.FILE_INPUT))
        file_dialog.send_keys(file_path)

    def get_uploaded_file_name(self) -> str:
        file_list = self._wait().until(EC.presence_of_element_located(self.FILE_CONTAINER))
        return file_list.text