from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

Locator = tuple[str, str]

class AnimatedButtonPage:
    START_ANIMATION_BUTTON = (By.ID, "animationButton")
    MOVING_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    STATUS_FIELD = (By.ID, "opstatus")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Return a WebDriverWait instance with the given timeout."""
        return WebDriverWait(self.driver, timeout)

    def _wait_for_animation_end(self, button: WebElement) -> None:
        """Wait until the spin animation on the button has finished."""
        self._wait(15).until(lambda _: "spin" not in button.get_attribute("class").split())

    def get_status(self) -> str:
        """Return the current text of the status field."""
        status_msg = self._wait().until(EC.visibility_of_element_located(self.STATUS_FIELD))
        return status_msg.text

    def click_start_button(self) -> None:
        """Click the button that starts the animation."""
        start_btn = self._wait().until(EC.element_to_be_clickable(self.START_ANIMATION_BUTTON))
        start_btn.click()

    def click_moving_button(self) -> None:
        """Wait for the animation to end, then click the moving button."""
        moving_btn = self._wait().until(EC.presence_of_element_located(self.MOVING_BUTTON))
        self._wait_for_animation_end(moving_btn)
        moving_btn.click()

