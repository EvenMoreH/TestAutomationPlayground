from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

Locator = tuple[str, str]


class MouseOverPage:
    FIRST_LINK = (By.CSS_SELECTOR, '.text-primary[title="Click me"]')
    FIRST_LINK_HOVER = (By.CSS_SELECTOR, '.text-warning[title="Active Link"]')
    SECOND_LINK = (By.CSS_SELECTOR, '.text-primary[title="Link Button"]')
    SECOND_LINK_HOVER = (By.CSS_SELECTOR, '.text-warning[title="Link Button"]')
    FIRST_LINK_CLICK_COUNT = (By.ID, "clickCount")
    SECOND_LINK_CLICK_COUNT = (By.ID, "clickButtonCount")

    def __init__(self, driver: WebDriver) -> None:
        """Store the Selenium driver for the page object."""
        self.driver = driver

    def _wait(self, timeout: int = 5) -> WebDriverWait:
        """Return an explicit wait configured for this driver."""
        return WebDriverWait(self.driver, timeout)

    def _hover(self, locator: Locator) -> None:
        """Hover over the element identified by the locator."""
        hoverable = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def get_counter_value(self, counter_element: Locator) -> int:
        """Return the current integer value for a click counter."""
        return int(self._wait().until(EC.visibility_of_element_located(counter_element)).text)

    def wait_for_counter_value(self, counter_element: Locator, expected_value: int) -> int:
        """Wait until the counter matches the expected value."""
        def counter_reached_expected_value(driver: WebDriver) -> int | bool:
            value = int(driver.find_element(*counter_element).text)
            return value if value == expected_value else False

        return self._wait().until(counter_reached_expected_value)

    def click_link(self, locator: Locator, locator_hovered: Locator, number_of_clicks: int) -> None:
        """Hover the base link and click the revealed active link."""
        self._hover(locator)

        link = self._wait().until(EC.element_to_be_clickable(locator_hovered))
        for _ in range(number_of_clicks):
            link.click()

