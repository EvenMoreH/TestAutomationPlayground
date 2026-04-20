# How to Run Tests - Quick Reference

## Setup

```bash
# Python dependencies (creates .venv automatically)
uv sync

# JavaScript dependencies
npm install

# Install Playwright browser binaries
uv run playwright install --with-deps chromium
npx playwright install --with-deps chromium
```

---

## Python Selenium

```bash
# All Selenium tests
uv run pytest exercises/python_selenium -v

# One exercise folder
uv run pytest exercises/python_selenium/Dynamic_ID/ -v

# Headless mode: uncomment --headless=new in exercises/python_selenium/conftest.py
```

Test files: `exercises/python_selenium/<Exercise>/test_*.py`
Fixture: `driver` (from exercises/python_selenium/conftest.py — Chrome via Selenium Manager)

---

## Python Playwright

```bash
# All Playwright tests
uv run pytest exercises/python_playwright -v

# One exercise folder
uv run pytest exercises/python_playwright/Dynamic_ID/ -v

# Run headed (visible browser)
uv run pytest exercises/python_playwright --headed

# Specific browser
uv run pytest exercises/python_playwright --browser firefox
```

Test files: `exercises/python_playwright/<Exercise>/test_*.py`
Fixture: `page` (built-in from pytest-playwright)

---

## JavaScript Playwright

```bash
# All JavaScript Playwright tests
npm run test:javascript

# One exercise folder
npx playwright test exercises/javascript_playwright/Visibility

# Run headed (visible browser)
npm run test:javascript:headed

# Open Playwright UI mode
npm run test:javascript:ui
```

Test files: `exercises/javascript_playwright/<Exercise>/test_*_playwright.spec.js`
Exercise files: `exercises/javascript_playwright/<Exercise>/*_playwright.js`
Framework: Playwright Test
Note: JavaScript exercise files are intentionally empty so you can write the solutions yourself.

---

## Run Everything

```bash
# Python (both Selenium + Playwright)
uv run pytest exercises/python_selenium exercises/python_playwright -v

# JavaScript Playwright
npm run test:javascript
```
