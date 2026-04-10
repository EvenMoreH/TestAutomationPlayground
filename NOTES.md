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

Test files: `exercises/java_playwright/<Exercise>/*Test.java`
Framework: JUnit 5

---

## Run Everything

```bash
# Python (both Selenium + Playwright)
uv run pytest exercises/python_selenium exercises/python_playwright -v

# Java
mvn test
```
