# How to Run Tests - Quick Reference

## Python Setup (one-time)

```bash
# Install dependencies (creates .venv automatically)
uv sync

# Install Playwright browser binaries
uv run playwright install --with-deps chromium
```

---

## Python Selenium

```bash
# All Selenium tests
uv run pytest exercises/ -v -k "Selenium"

# One exercise folder
uv run pytest exercises/Dynamic_ID/Dynamic_ID_Python_Selenium/ -v

# Headless mode: uncomment --headless=new in conftest.py
```

Test files: `exercises/<Exercise>/<Exercise>_Python_Selenium/test_*.py`
Fixture: `driver` (from root conftest.py — Chrome via Selenium Manager)

---

## Python Playwright

```bash
# All Playwright tests
uv run pytest exercises/ -v -k "Playwright"

# One exercise folder
uv run pytest exercises/Dynamic_ID/Dynamic_ID_Python_Playwright/ -v

# Run headed (visible browser)
uv run pytest exercises/ --headed

# Specific browser
uv run pytest exercises/ --browser firefox
```

Test files: `exercises/<Exercise>/<Exercise>_Python_Playwright/test_*.py`
Fixture: `page` (built-in from pytest-playwright)

---

## Java Playwright

```bash
# All Java tests
mvn test

# One specific test class
mvn test -Dtest=DynamicIdTest

# Tests matching a pattern
mvn test -Dtest="*Click*"

# Clean build + test
mvn clean test
```

Test files: `exercises/<Exercise>/<Exercise>_Java_Playwright/*Test.java`
Framework: JUnit 5

---

## Run Everything

```bash
# Python (both Selenium + Playwright)
uv run pytest exercises/ -v

# Java
mvn test
```
