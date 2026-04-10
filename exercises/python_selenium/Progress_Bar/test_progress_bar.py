from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from progress_bar import ProgressBarPage

def test_progress_bar(driver: WebDriver):
    progress_bar_page = ProgressBarPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/progressbar")
    assert page.is_loaded()

    progress_bar_page.click_start_btn()
    progress_bar_page.click_stop_btn()

    progress = progress_bar_page.get_progress_value()
    assert progress == "75%"