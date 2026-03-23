from selenium.webdriver.remote.webdriver import WebDriver
from file_upload_selenium import FileUploadPage

def test_file_upload_selenium(driver: WebDriver):
    file_upload_page = FileUploadPage(driver)

    driver.get("")
