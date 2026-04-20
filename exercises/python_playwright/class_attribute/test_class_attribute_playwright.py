from playwright.sync_api import Page
from exercises.python_playwright.navbar import Navbar
from exercises.python_playwright.class_attribute.class_attribute_playwright import ClassAttribute

def test_click_class_attr_button(page: Page):
    cap = ClassAttribute(page)
    navbar = Navbar(page)

    cap.open()
    navbar.page_loaded()

    message = cap.click_primary_button()
    assert message == "Primary button pressed"