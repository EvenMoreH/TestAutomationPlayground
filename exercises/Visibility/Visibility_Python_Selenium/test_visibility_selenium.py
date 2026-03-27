from selenium.webdriver.remote.webdriver import WebDriver
from visibility_selenium import VisibilityPage

def test_removed_btn_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("http://uitestingplayground.com/visibility")

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_removed_btn()
    assert is_invisible == True

def test_zero_width_btn_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("http://uitestingplayground.com/visibility")

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_zero_width_btn()
    assert is_invisible == True

def test_overlapped_btn_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("http://uitestingplayground.com/visibility")

    visibility_page.hide_btn_click()
    is_invisible= visibility_page.is_invisible_overlapped_btn()
    assert is_invisible == True

def test_opacity_zero_btn_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("http://uitestingplayground.com/visibility")

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_opacity_zero_btn()
    assert is_invisible == True

def test_visibility_hidden_btn_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("http://uitestingplayground.com/visibility")

    visibility_page.hide_btn_click()
    is_invisible = visibility_page.is_invisible_visibility_hidden_btn()
    assert is_invisible == True

def test_none_btn_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("http://uitestingplayground.com/visibility")

    visibility_page.hide_btn_click()
    pass

def test_offscreen_btn_visibility_selenium(driver: WebDriver):
    visibility_page = VisibilityPage(driver)

    driver.get("http://uitestingplayground.com/visibility")

    visibility_page.hide_btn_click()
    pass
