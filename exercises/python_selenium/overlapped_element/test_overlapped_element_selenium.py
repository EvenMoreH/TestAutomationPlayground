from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.overlapped_element.overlapped_element_selenium import (
    TEST_ID_VALUE,
    TEST_NAME_VALUE,
    OverlappedElementPage,
)

def test_fill_out_form_overlapped_element_selenium(driver: WebDriver):
    oep = OverlappedElementPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/overlapped")
    assert page.is_loaded()

    oep.fill_out_id()
    oep.fill_out_name()

    assert oep.get_id_value() == TEST_ID_VALUE
    assert oep.get_name_value() == TEST_NAME_VALUE
