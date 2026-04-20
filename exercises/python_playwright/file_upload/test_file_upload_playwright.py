from pathlib import Path
from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.file_upload.file_upload_playwright import FileUploadPage

test_file_dir: str | Path = "exercises/python_playwright/file_upload/"
test_files: list[str | Path] = [
    test_file_dir + "test_doc.txt",
    test_file_dir + "test_doc2.txt",
    test_file_dir + "test_doc3.txt",
    ]

def test_file_upload(page: Page):
    upload_page = FileUploadPage(page)
    navbar = Navbar(page)

    upload_page.open()
    navbar.page_loaded()

    upload_page.input_files(test_files)
    list_of_files = upload_page.get_list_of_uploaded_files()
    assert "test_doc.txt" and "test_doc2.txt" and "test_doc3.txt" in list_of_files