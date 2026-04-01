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

    def hide_btn_click(self) -> None:
        """Click the Hide button to reveal the visibility scenarios."""
        hide_btn = self._wait().until(EC.element_to_be_clickable(self.HIDE_BTN))
        hide_btn.click()

    def is_invisible_removed_btn(self) -> bool:
        """Verify the removed button is not visible."""
        self._wait().until(EC.invisibility_of_element_located(self.REMOVED_BTN))
        return True

    def is_invisible_zero_width_btn(self) -> bool:
        """Verify the zero-width button is not visible."""
        self._wait().until(EC.invisibility_of_element_located(self.ZERO_W_BUTTON))
        return True

    def is_invisible_overlapped_btn(self) -> bool:
        """Verify the overlapped button is not visible."""
        overlapped_button = self.driver.find_element(*self.OVERLAPPED_BTN)

        if not overlapped_button.is_displayed():
            return True

        rect = overlapped_button.rect
        if rect["width"] == 0 or rect["height"] == 0:
            return True

        center_x = rect["x"] + rect["width"] / 2
        center_y = rect["y"] + rect["height"] / 2

        top_element = self.driver.execute_script(
            "return document.elementFromPoint(arguments[0], arguments[1]);", center_x, center_y)

        if top_element is None:
            return True

        is_covered = self.driver.execute_script(
            "return arguments[0] === arguments[1] || arguments[0].contains(arguments[1]);", overlapped_button, top_element)

        if is_covered:
            return False
        return True

    def is_invisible_opacity_zero_btn(self) -> bool:
        """Verify the opacity-zero button is not visible."""
        self._wait().until(EC.invisibility_of_element_located(self.OPACITY_ZERO_BTN))
        return True

    def is_invisible_visibility_hidden_btn(self) -> bool:
        """Verify the visibility-hidden button is not visible."""
        self._wait().until(EC.invisibility_of_element_located(self.VISIBILITY_HIDDEN_BTN))
        return True

    def is_invisible_none_btn(self) -> bool:
        """Verify the display-none button is not visible."""
        self._wait().until(EC.invisibility_of_element_located(self.NONE_BTN))
        return True

    def is_invisible_offscreen_btn(self) -> bool:
        """Verify the offscreen button is not fully within viewport."""
        offscreen_button = self.driver.find_element(*self.OFFSCREEN_BTN)

        return self.driver.execute_script(
            """
            const rect = arguments[0].getBoundingClientRect();
            const viewWidth = window.innerWidth || document.documentElement.clientWidth;
            const viewHeight = window.innerHeight || document.documentElement.clientHeight;

            return !(
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= viewHeight &&
                rect.right <= viewWidth
            );
            """,
            offscreen_button,
        )
