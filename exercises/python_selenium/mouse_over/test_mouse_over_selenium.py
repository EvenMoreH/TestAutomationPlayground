from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.mouse_over.mouse_over_selenium import MouseOverPage

URL = "http://uitestingplayground.com/mouseover"

def test_mouse_over_first_link_selenium(driver: WebDriver) -> None:
    mop = MouseOverPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    initial_counter_value = mop.get_counter_value(mop.FIRST_LINK_CLICK_COUNT)
    assert initial_counter_value == 0

    mop.click_link(mop.FIRST_LINK, mop.FIRST_LINK_HOVER, 2)

    new_counter_value = mop.wait_for_counter_value(mop.FIRST_LINK_CLICK_COUNT, 2)
    assert new_counter_value == 2

def test_mouse_over_second_link_selenium(driver: WebDriver) -> None:
    mop = MouseOverPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    initial_counter_value = mop.get_counter_value(mop.SECOND_LINK_CLICK_COUNT)
    assert initial_counter_value == 0

    mop.click_link(mop.SECOND_LINK, mop.SECOND_LINK_HOVER, 2)

    new_counter_value = mop.wait_for_counter_value(mop.SECOND_LINK_CLICK_COUNT, 2)
    assert new_counter_value == 2

def test_mouse_over_both_links_selenium(driver: WebDriver) -> None:
    mop = MouseOverPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    initial_counter_value_1 = mop.get_counter_value(mop.FIRST_LINK_CLICK_COUNT)
    assert initial_counter_value_1 == 0

    initial_counter_value_2 = mop.get_counter_value(mop.SECOND_LINK_CLICK_COUNT)
    assert initial_counter_value_2 == 0

    mop.click_link(mop.FIRST_LINK, mop.FIRST_LINK_HOVER, 1)
    mop.click_link(mop.SECOND_LINK, mop.SECOND_LINK_HOVER, 1)

    new_counter_value_1 = mop.wait_for_counter_value(mop.FIRST_LINK_CLICK_COUNT, 1)
    assert new_counter_value_1 == 1

    new_counter_value_2 = mop.wait_for_counter_value(mop.SECOND_LINK_CLICK_COUNT, 1)
    assert new_counter_value_2 == 1