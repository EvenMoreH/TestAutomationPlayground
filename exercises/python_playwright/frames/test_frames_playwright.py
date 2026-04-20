from playwright.sync_api import Page, expect
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.frames.frames_playwright import FramesPage


RESULT_PREFIX = "Button pressed: "

def test_click_buttons_in_frames(page: Page) -> None:
    frames_page = FramesPage(page)
    navbar = Navbar(page)

    frames_page.open()
    navbar.page_loaded()

    expect(frames_page.outer_result).to_have_text("")
    expect(frames_page.inner_result).to_have_text("")

    frames_page.click_edit_button_in_frame(frames_page.outer_frame)
    expect(frames_page.outer_result).to_have_text(RESULT_PREFIX + "Edit")

    frames_page.click_submit_button_in_frame(frames_page.outer_frame)
    expect(frames_page.outer_result).to_have_text(RESULT_PREFIX + "Submit")

    frames_page.click_click_me_button_in_frame(frames_page.outer_frame)
    expect(frames_page.outer_result).to_have_text(RESULT_PREFIX + "Click me")

    frames_page.click_primary_button_in_frame(frames_page.outer_frame)
    expect(frames_page.outer_result).to_have_text(RESULT_PREFIX + "Primary")

    frames_page.click_edit_button_in_frame(frames_page.inner_frame)
    expect(frames_page.inner_result).to_have_text(RESULT_PREFIX + "Edit")

    frames_page.click_submit_button_in_frame(frames_page.inner_frame)
    expect(frames_page.inner_result).to_have_text(RESULT_PREFIX + "Submit")

    frames_page.click_click_me_button_in_frame(frames_page.inner_frame)
    expect(frames_page.inner_result).to_have_text(RESULT_PREFIX + "Click me")

    frames_page.click_primary_button_in_frame(frames_page.inner_frame)
    expect(frames_page.inner_result).to_have_text(RESULT_PREFIX + "Primary")