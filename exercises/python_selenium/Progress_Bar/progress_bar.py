from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProgressBarPage:
    START_BTN = (By.ID, "startButton")
    STOP_BTN = (By.ID, "stopButton")
    PROGRESS_BAR = (By.ID, "progressBar")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # added non-standard poll frequency to counter fast update time of progress bar
    def _wait(self, timeout: int = 5, poll_frequency: float = 0.02) -> WebDriverWait:
        """Create a wait helper with a custom poll frequency."""
        return WebDriverWait(self.driver, timeout, poll_frequency)

    def get_progress_value(self) -> str:
        """Wait until the progress bar reaches 75% and return its text."""
        self._wait(25).until(
            lambda driver: int(driver.find_element(*self.PROGRESS_BAR).get_attribute("aria-valuenow")) >= 75
        )
        return self.driver.find_element(*self.PROGRESS_BAR).text.strip()

    def click_start_btn(self) -> None:
        """Click the start button to begin the progress bar."""
        start_button = self._wait().until(EC.element_to_be_clickable(self.START_BTN))
        start_button.click()

    def click_stop_btn(self) -> None:
        """Click the stop button once progress reaches 75%."""
        stop_button = self._wait(25).until(EC.element_to_be_clickable(self.STOP_BTN))

        progress = self.get_progress_value()
        if progress == "75%":
            stop_button.click()
