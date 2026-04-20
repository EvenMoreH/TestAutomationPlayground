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

    _ID_FIELD: Locator = (By.ID, "id")
    _NAME_FIELD: Locator = (By.ID, "name")

    def __init__(self, driver: WebDriver) -> None:
        """Store the browser driver used to interact with the page."""
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Create a wait helper for page interactions."""
        return WebDriverWait(self.driver, timeout)

    def _scroll_to(self, locator: Locator, x: int, y: int) -> None:
        """Scroll the container around the target element by the given offsets."""
        element = self._wait().until(EC.presence_of_element_located(locator))
        container = element.find_element(By.XPATH, "./..")
        origin = ScrollOrigin.from_element(container)
        ActionChains(self.driver).scroll_from_origin(origin, x, y).perform()

    def _fill_field(self, locator: Locator, value: str) -> None:
        """Clear and populate the given input field."""
        element = self._wait().until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def _get_field_value(self, locator: Locator) -> str:
        """Return the current value of the given input field."""
        element = self._wait().until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")

    def fill_out_id(self) -> None:
        """Clear and populate the ID input field."""
        self._fill_field(self._ID_FIELD, TEST_ID_VALUE)

    def fill_out_name(self) -> None:
        """Scroll the name field into view, then clear and populate it."""
        self._scroll_to(self._NAME_FIELD, 0, 50)
        self._fill_field(self._NAME_FIELD, TEST_NAME_VALUE)

    def get_id_value(self) -> str:
        """Return the current value of the ID input field."""
        return self._get_field_value(self._ID_FIELD)

    def get_name_value(self) -> str:
        """Return the current value of the name input field."""
        return self._get_field_value(self._NAME_FIELD)