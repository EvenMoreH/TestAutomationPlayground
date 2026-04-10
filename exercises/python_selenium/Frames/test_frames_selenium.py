from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from frames_selenium import FramesPage

URL = "http://uitestingplayground.com/frames"
RESULT = "Button pressed: "

def test_frames_outer_buttons_selenium(driver: WebDriver):
    frames_page = FramesPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    frames_page.switch_to_outer_frame()
    frames_page.click_edit_button()
    frames_page.wait_for_result_update(RESULT + "Edit")
    assert frames_page.read_result() == RESULT + "Edit"

    frames_page.click_submit_button()
    frames_page.wait_for_result_update(RESULT + "Submit")
    assert frames_page.read_result() == RESULT + "Submit"

    frames_page.click_click_me_button()
    frames_page.wait_for_result_update(RESULT + "Click me")
    assert frames_page.read_result() == RESULT + "Click me"

    frames_page.click_primary_button()
    frames_page.wait_for_result_update(RESULT + "Primary")
    assert frames_page.read_result() == RESULT + "Primary"

def test_frames_inner_buttons_selenium(driver: WebDriver):
    frames_page = FramesPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    frames_page.switch_to_outer_frame()
    frames_page.switch_to_inner_frame()
    frames_page.click_edit_button()
    frames_page.wait_for_result_update(RESULT + "Edit")
    assert frames_page.read_result() == RESULT + "Edit"

    frames_page.click_submit_button()
    frames_page.wait_for_result_update(RESULT + "Submit")
    assert frames_page.read_result() == RESULT + "Submit"

    frames_page.click_click_me_button()
    frames_page.wait_for_result_update(RESULT + "Click me")
    assert frames_page.read_result() == RESULT + "Click me"

    frames_page.click_primary_button()
    frames_page.wait_for_result_update(RESULT + "Primary")
    assert frames_page.read_result() == RESULT + "Primary"