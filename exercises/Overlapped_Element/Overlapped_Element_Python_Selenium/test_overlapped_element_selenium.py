from selenium.webdriver.remote.webdriver import WebDriver
from exercises.base_page_selenium import BasePage
from overlapped_element_selenium import TEST_ID_VALUE, TEST_NAME_VALUE, OverlappedElementPage

def test_fill_out_form_overlapped_element_selenium(driver: WebDriver):
    oep = OverlappedElementPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/overlapped")
    assert page.is_loaded()

    oep.fill_out_id(oep.ID_FIELD)
    oep.scroll(oep.NAME_FIELD, 0, 50)
    oep.fill_out_name(oep.NAME_FIELD)

    id_value = oep.field_value(oep.ID_FIELD)
    assert id_value == TEST_ID_VALUE
    name_value = oep.field_value(oep.NAME_FIELD)
    assert name_value == TEST_NAME_VALUE
