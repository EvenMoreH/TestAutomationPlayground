from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.shadowroot import ShadowRoot

class ShadowDomPage:
    GUID_GENERATOR = (By.CSS_SELECTOR, "guid-generator")
    GUID_FIELD = (By.CLASS_NAME, "edit-field")
    GUID_GENERATE_BTN = (By.ID, "buttonGenerate")
    GUID_COPY = (By.ID, "buttonCopy")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def _shadow_root(self) -> ShadowRoot:
        host = self._wait().until(EC.presence_of_element_located(self.GUID_GENERATOR))
        return host.shadow_root

    def _shadow_wait(self, timeout: int = 5) -> WebDriverWait:
        return WebDriverWait(self._shadow_root(), timeout)

    def clear_guid_input_field(self) -> None:
        input_field = self._shadow_wait().until(EC.visibility_of_element_located(self.GUID_FIELD))
        input_field.clear()

    def get_guid_field_value(self) -> str:
        value = self._shadow_wait().until(EC.visibility_of_element_located(self.GUID_FIELD)).get_attribute("value")
        return value.strip() if value else ""

    def generate_guid(self) -> None:
        generate_btn = self._shadow_wait().until(EC.element_to_be_clickable(self.GUID_GENERATE_BTN))
        generate_btn.click()

    def copy_guid_to_clipboard(self) -> None:
        copy_button = self._shadow_wait().until(EC.element_to_be_clickable(self.GUID_COPY))
        copy_button.click()

    def paste_guid_value(self) -> None:
        guid_input_field = self._shadow_wait().until(EC.visibility_of_element_located(self.GUID_FIELD))
        guid_input_field.send_keys(Keys.CONTROL, "v")