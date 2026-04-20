from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.frames.frames_selenium import FramesPage

URL = "http://uitestingplayground.com/frames"
RESULT_PREFIX = "Button pressed: "

def test_frames_buttons_selenium(driver: WebDriver):
    frames_page = FramesPage(driver)
    page = BasePage(driver)

    driver.get(URL)
    assert page.is_loaded()

    frames_page.switch_to_outer_frame()
    frames_page.assert_result("")
    frames_page.switch_to_inner_frame()
    frames_page.assert_result("")

    frames_page.switch_to_parent_frame()

    frames_page.click_edit_button()
    frames_page.assert_result(RESULT_PREFIX + "Edit")

    frames_page.click_submit_button()
    frames_page.assert_result(RESULT_PREFIX + "Submit")

    frames_page.click_click_me_button()
    frames_page.assert_result(RESULT_PREFIX + "Click me")

    frames_page.click_primary_button()
    frames_page.assert_result(RESULT_PREFIX + "Primary")

    frames_page.switch_to_inner_frame()

    frames_page.click_edit_button()
    frames_page.assert_result(RESULT_PREFIX + "Edit")

    frames_page.click_submit_button()
    frames_page.assert_result(RESULT_PREFIX + "Submit")

    frames_page.click_click_me_button()
    frames_page.assert_result(RESULT_PREFIX + "Click me")

    frames_page.click_primary_button()
    frames_page.assert_result(RESULT_PREFIX + "Primary")