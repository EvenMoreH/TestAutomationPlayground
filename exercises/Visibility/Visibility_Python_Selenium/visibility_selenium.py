from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VisibilityPage:
    HIDE_BTN = (By.ID, "hideButton")
    REMOVED_BTN = (By.ID, "removedButton")
    ZERO_W_BUTTON = (By.ID, "zeroWidthButton")
    OVERLAPPED_BTN = (By.ID, "overlappedButton")
    OPACITY_ZERO_BTN = (By.ID, "transparentButton")
    VISIBILITY_HIDDEN_BTN = (By.ID, "invisibleButton")
    NONE_BTN = (By.ID, "notdisplayedButton")
    OFFSCREEN_BTN = (By.ID, "offscreenButton")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def hide_btn_click(self):
        hide_btn = self._wait().until(EC.element_to_be_clickable(self.HIDE_BTN))
        hide_btn.click()

    def is_invisible_removed_btn(self):
        removed_btn = self._wait().until(EC.invisibility_of_element_located(self.REMOVED_BTN))
        return removed_btn

    def is_invisible_zero_width_btn(self):
        pass

    def is_invisible_overlapped_btn(self):
        pass

    def is_invisible_opacity_zero_btn(self):
        pass

    def is_invisible_visibility_hidden_btn(self):
        pass

    def is_invisible_none_btn(self):
        pass

    def is_invisible_offscreen_btn(self):
        pass

