"""Reusable explicit-wait helpers for Selenium page objects.

Use this module to avoid repeating `WebDriverWait(...).until(...)` syntax
while still keeping per-element timeout control.
"""

from __future__ import annotations

from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = tuple[str, str]


class SeleniumWaits:
    def __init__(self, driver: WebDriver, default_timeout: int = 10, poll_frequency: float = 0.2):
        self.driver = driver
        self.default_timeout = default_timeout
        self.poll_frequency = poll_frequency

    def _wait(self, timeout: Optional[int] = None) -> WebDriverWait:
        return WebDriverWait(
            self.driver,
            timeout if timeout is not None else self.default_timeout,
            poll_frequency=self.poll_frequency,
        )

    def present(self, locator: Locator, timeout: Optional[int] = None):
        return self._wait(timeout).until(EC.presence_of_element_located(locator))

    def visible(self, locator: Locator, timeout: Optional[int] = None):
        return self._wait(timeout).until(EC.visibility_of_element_located(locator))

    def clickable(self, locator: Locator, timeout: Optional[int] = None):
        return self._wait(timeout).until(EC.element_to_be_clickable(locator))

    def invisible(self, locator: Locator, timeout: Optional[int] = None):
        return self._wait(timeout).until(EC.invisibility_of_element_located(locator))
