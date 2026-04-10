from playwright.sync_api import Page, expect

class Navbar:
    def __init__(self, page: Page):
        self.page = page
        self.navbar = page.locator(".navbar-brand")
        self.footer = page.locator("#footer-content")

    def page_loaded(self) -> None:
        expect(self.navbar).to_be_visible()
        expect(self.footer).to_be_visible()