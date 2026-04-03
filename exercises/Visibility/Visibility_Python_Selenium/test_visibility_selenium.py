from selenium.webdriver.remote.webdriver import WebDriver
from visibility_selenium import VisibilityPage
from exercises.base_page_selenium import BasePage


def test_removed_btn_visibility_selenium(driver: WebDriver):
    """Verify the removed button becomes invisible after clicking Hide."""
    visibility_page = VisibilityPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/visibility")
    assert page.is_loaded()

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_removed_btn()
    assert is_invisible == True


def test_zero_width_btn_visibility_selenium(driver: WebDriver):
    """Verify the zero-width button becomes invisible after clicking Hide."""
    visibility_page = VisibilityPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/visibility")
    assert page.is_loaded()

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_zero_width_btn()
    assert is_invisible == True


def test_overlapped_btn_visibility_selenium(driver: WebDriver):
    """Verify the overlapped button is treated as invisible after clicking Hide."""
    visibility_page = VisibilityPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/visibility")
    assert page.is_loaded()

    visibility_page.hide_btn_click()
    is_invisible= visibility_page.is_invisible_overlapped_btn()
    assert is_invisible == True


def test_opacity_zero_btn_visibility_selenium(driver: WebDriver):
    """Verify the opacity-zero button becomes invisible after clicking Hide."""
    visibility_page = VisibilityPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/visibility")
    assert page.is_loaded()

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_opacity_zero_btn()
    assert is_invisible == True


def test_visibility_hidden_btn_visibility_selenium(driver: WebDriver):
    """Verify the visibility-hidden button becomes invisible after clicking Hide."""
    visibility_page = VisibilityPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/visibility")
    assert page.is_loaded()

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_visibility_hidden_btn()
    assert is_invisible == True


def test_none_btn_visibility_selenium(driver: WebDriver):
    """Verify the display-none button becomes invisible after clicking Hide."""
    visibility_page = VisibilityPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/visibility")
    assert page.is_loaded()

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_none_btn()
    assert is_invisible == True


def test_offscreen_btn_visibility_selenium(driver: WebDriver):
    """
    Verify the offscreen button is reported as not fully inside the viewport,
    thus not visible to the users.
    """
    visibility_page = VisibilityPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/visibility")
    assert page.is_loaded()

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_offscreen_btn()
    assert is_invisible == True
