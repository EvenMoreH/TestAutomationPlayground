from selenium.webdriver.remote.webdriver import WebDriver
from progress_bar import ProgressBarPage

def test_progress_bar(driver: WebDriver):
    progress_bar_page = ProgressBarPage(driver)

    driver.get("http://uitestingplayground.com/progressbar")

    progress_bar_page.click_start_btn()
    progress_bar_page.click_stop_btn()

    progress = progress_bar_page.get_progress_value()
    assert progress == "75%"