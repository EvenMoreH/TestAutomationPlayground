"""
Shared pytest fixtures for the TestAutomationPlayground project.

Selenium tests use the `driver` fixture defined here.
Playwright tests use the built-in `page` fixture from pytest-playwright.

Selenium 4+ includes Selenium Manager which automatically downloads
the correct ChromeDriver — no need for webdriver-manager.
"""

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Create a Selenium Chrome WebDriver instance for each test."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
