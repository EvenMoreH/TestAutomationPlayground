from playwright.sync_api import Page, expect


class MouseOverPage:
    def __init__(self, page: Page):
        self.page = page
        self.click_me_btn = page.get_by_title("Click Me")
        self.click_me_btn_active = page.get_by_title("Active Link")
        self.link_btn = page.get_by_title("Link Button")
        self.click_me_click_count = page.locator("#clickCount")
        self.link_btn_click_count = page.locator("#clickButtonCount")

    def open(self) -> None:
        self.page.goto("http://uitestingplayground.com/mouseover")

    def doubleclick_button_click_me(self) -> None:
        self.click_me_btn.hover()
        expect(self.click_me_btn_active).to_have_class("text-warning")
        self.click_me_btn_active.dblclick()

    def doubleclick_button_link_button(self) -> None:
        self.link_btn.hover()
        expect(self.link_btn).to_have_class("text-warning")
        self.link_btn.dblclick()