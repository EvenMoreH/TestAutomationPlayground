import { expect } from "@playwright/test";

export class Navbar {
    /**
     *
     * @param {import('@playwright/test').Page} page
     */
    constructor(page) {
        this.page = page;
        this.navbar = page.locator(".navbar-brand");
        this.footer = page.locator("#footer-content");
    }

    async pageLoaded() {
        expect(this.navbar).toBeVisible();
        expect(this.footer).toBeVisible();
    }
}
