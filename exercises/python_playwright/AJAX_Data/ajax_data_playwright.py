from playwright.sync_api import Page

class AjaxData:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.ajax_button = page.get_by_role("button", name="Button")
        self.ajax_status = page.locator(".bg-success")

    def open(self) -> None:
        self.page.goto("http://uitestingplayground.com/ajax")

    def click_ajax_button(self) -> None:
        self.ajax_button.click()