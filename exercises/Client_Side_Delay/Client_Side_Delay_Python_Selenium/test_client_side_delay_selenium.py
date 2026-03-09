from selenium.webdriver.remote.webdriver import WebDriver
from client_side_delay_selenium import ClientSideDelay

def test_ajax_data_loading(driver: WebDriver):
    ajax_data_page = ClientSideDelay(driver)

    driver.get("http://uitestingplayground.com/clientdelay")

    ajax_data_page.click_ajax_button()
    message = ajax_data_page.get_success_message()
    assert message == "Data calculated on the client side."