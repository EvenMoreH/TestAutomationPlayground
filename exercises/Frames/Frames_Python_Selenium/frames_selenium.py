from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Locator = tuple[str, str]

class FramesPage:
    OUTER_FRAME = (By.ID, "frame-outer")
    INNER_FRAME = (By.ID, "frame-inner")
    EDIT_BUTTON = (By.CSS_SELECTOR, "[data-action='edit']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Submit']")
    CLICK_ME_BUTTON = (By.NAME, "my-button")
    PRIMARY_BUTTON = (By.XPATH, ".//button[@class='btn-class']")
    RESULT_BANNER = (By.ID, "result")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        """Return a WebDriverWait instance with the given timeout."""
        return WebDriverWait(self.driver, timeout)

    def _switch_frame(self, locator: Locator) -> None:
        """Wait for a frame to be present and switch to it."""
        iframe = self._wait().until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(iframe)

    def _click(self, button: Locator) -> None:
        """Wait for a button to be clickable and click it."""
        self._wait().until(EC.element_to_be_clickable(button)).click()

    def switch_to_outer_frame(self) -> None:
        """Switch the driver context to the outer frame."""
        self._switch_frame(self.OUTER_FRAME)

    def switch_to_inner_frame(self) -> None:
        """Switch the driver context to the inner frame."""
        self._switch_frame(self.INNER_FRAME)

    def wait_for_result_update(self, expected_result: str) -> None:
        """Wait until the result banner contains the expected text."""
        self._wait(2).until(EC.text_to_be_present_in_element(self.RESULT_BANNER, expected_result))

    def read_result(self) -> str:
        """Return the current text of the result banner."""
        return self._wait().until(EC.presence_of_element_located(self.RESULT_BANNER)).text

    def click_edit_button(self) -> None:
        """Click the Edit button."""
        self._click(self.EDIT_BUTTON)

    def click_submit_button(self) -> None:
        """Click the Submit button."""
        self._click(self.SUBMIT_BUTTON)

    def click_click_me_button(self) -> None:
        """Click the Click Me button."""
        self._click(self.CLICK_ME_BUTTON)

    def click_primary_button(self) -> None:
        """Click the primary button."""
        self._click(self.PRIMARY_BUTTON)