from playwright.sync_api import Error, Locator, Page


class VisibilityPage:
    """Page object for the Visibility exercise."""

    def __init__(self, page: Page):
        """Initialize the page and button locators."""
        self.page = page
        self.hide_button = page.get_by_role("button", name="Hide")
        self.removed_button = page.locator("#removedButton")
        self.zero_width_button = page.locator("#zeroWidthButton")
        self.overlapped_button = page.locator("#overlappedButton")
        self.zero_opacity_button = page.locator("#transparentButton")
        self.hidden_button = page.locator("#invisibleButton")
        self.none_button = page.locator("#notdisplayedButton")
        self.offscreen_button = page.locator("#offscreenButton")

    def open(self) -> None:
        """Open the Visibility exercise page."""
        self.page.goto("http://uitestingplayground.com/visibility")

    def click_hide_button(self) -> None:
        """Click the button that hides the target buttons."""
        self.hide_button.click()

    def is_invisible_for_user(self, locator: Locator) -> tuple[bool | str]:
        """Return invisibility status and the first matching reason."""
        # built in is_visible() check
        if not locator.is_visible():
            return True, "Playwright invisible"

        # opacity check
        opacity = float(locator.evaluate("el => getComputedStyle(el).opacity"))
        if opacity == 0:
            return True, "Opacity = 0"

        # offscreen check
        offscreen = locator.evaluate(
        """
        el => {
            const r = el.getBoundingClientRect();
            return (
                r.bottom < 0 ||
                r.right < 0 ||
                r.top > window.innerHeight ||
                r.left > window.innerWidth
            );
        }
        """)
        if offscreen:
            return True, "Button Offscreen"

        # not clickable by user
        try:
            locator.click(trial=True, timeout=2000)
        except Error:
            return True, "Button Overlapped"

        # passed all checks
        return False, "Button visible to users"