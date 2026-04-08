"""Page object for the Overlapped Element Selenium exercise."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains

Locator = tuple[str, str]
TEST_ID_VALUE = "test-id"
TEST_NAME_VALUE = "test-name"


class OverlappedElementPage:
    """Encapsulates interactions with the overlapped element exercise page."""

    ID_FIELD = (By.ID, "id")
    NAME_FIELD = (By.ID, "name")

    def __init__(self, driver: WebDriver) -> None:
        """Store the browser driver used to interact with the page."""
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def scroll(self, locator: Locator, x: int, y: int) -> None:
        """Scroll the container around the target element by the given offsets."""
        element = self._wait().until(EC.presence_of_element_located(locator))
        container = element.find_element(By.XPATH, "./..")  # strategy to target container of element being targeted
        origin = ScrollOrigin.from_element(container)
        ActionChains(self.driver).scroll_from_origin(origin, x, y).perform()

    def fill_out_id(self, id_locator: Locator) -> None:
        """Clear and populate the ID input field."""
        id_element = self._wait().until(EC.visibility_of_element_located(id_locator))
        id_element.clear()
        id_element.send_keys(TEST_ID_VALUE)

    def fill_out_name(self, name_locator: Locator) -> None:
        """Clear and populate the name input field."""
        name_element = self._wait().until(EC.visibility_of_element_located(name_locator))
        name_element.clear()
        name_element.send_keys(TEST_NAME_VALUE)

    def field_value(self, locator: Locator) -> str:
        """Return the current value of the requested input field."""
        element = self._wait().until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")