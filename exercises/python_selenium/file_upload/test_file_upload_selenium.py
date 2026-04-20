from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver

from exercises.python_selenium.base_page_selenium import BasePage
from exercises.python_selenium.file_upload.file_upload_selenium import FileUploadPage

FILE = "test_doc.txt"
FILE_PATH = str(Path(__file__).with_name(FILE).resolve())

def test_file_upload_selenium(driver: WebDriver):
    file_upload_page = FileUploadPage(driver)
    page = BasePage(driver)

    driver.get("http://uitestingplayground.com/upload")
    assert page.is_loaded()

    file_upload_page.upload_file(FILE_PATH)
    assert file_upload_page.get_uploaded_file_name() == FILE