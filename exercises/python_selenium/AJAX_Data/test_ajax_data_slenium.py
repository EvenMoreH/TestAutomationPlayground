from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from ajax_data_slenium import AjaxData

def test_ajax_data_loading(driver: WebDriver):
    ajax_data_page = AjaxData(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/ajax")
    assert page.is_loaded()

    ajax_data_page.click_ajax_button()
    message = ajax_data_page.get_success_message()
    assert message == "Data loaded with AJAX get request."