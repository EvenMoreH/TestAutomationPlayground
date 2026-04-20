from pathlib import Path
from playwright.sync_api import Page


class FileUploadPage:
    def __init__(self, page: Page):
        """
        Initialize locators for the upload page and embedded upload frame.
        Locators are inside iframe, thus self.iframe is used for this exercise.
        """
        self.page = page
        self.iframe = page.frame_locator("iframe")
        self.input_element = self.iframe.locator("#browse")
        self.uploaded_files = self.iframe.locator(".file-item")


    def open(self) -> None:
        """Navigate to the file upload exercise page."""
        self.page.goto("http://uitestingplayground.com/upload")


    def input_files(self, files: list[str | Path]) -> None:
        """Upload one or more files through the file input control."""
        self.input_element.set_input_files(files)


    def get_list_of_uploaded_files(self) -> list[str]:
        """Return the displayed names of the uploaded files."""
        return self.uploaded_files.all_text_contents()