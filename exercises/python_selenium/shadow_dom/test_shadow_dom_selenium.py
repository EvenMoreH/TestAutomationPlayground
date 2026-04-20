from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.shadow_dom.shadow_dom_selenium import ShadowDomPage

def test_shadow_dom_selenium(driver: WebDriver):
    shadow_dom_page = ShadowDomPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/shadowdom")
    assert page.is_loaded()

    shadow_dom_page.clear_guid_input_field()
    shadow_dom_page.generate_guid()
    generated_guid_value = shadow_dom_page.get_guid_field_value()
    assert generated_guid_value != ""

    shadow_dom_page.copy_guid_to_clipboard()
    shadow_dom_page.clear_guid_input_field()
    shadow_dom_page.paste_guid_value()

    copy_paste_guid_value = shadow_dom_page.get_guid_field_value()

    assert generated_guid_value == copy_paste_guid_value