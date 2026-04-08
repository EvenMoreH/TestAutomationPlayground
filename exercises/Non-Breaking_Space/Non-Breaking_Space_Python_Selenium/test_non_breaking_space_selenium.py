from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from non_breaking_space_selenium import NonBreakingSpacePage

def test_non_breaking_space_selenium(driver: WebDriver) -> None:
    """
    Verifies the nbsp exercise button can be clicked.
    For the purpose of this exercise, prints which locator worked.
    """
    non_breaking_space_page = NonBreakingSpacePage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/nbsp")
    assert page.is_loaded()

    click_result = non_breaking_space_page.click_button()
    assert click_result != None
    print(click_result)
