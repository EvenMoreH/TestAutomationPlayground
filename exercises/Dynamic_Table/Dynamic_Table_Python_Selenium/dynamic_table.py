from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicTablePage:
    TABLE = (By.CSS_SELECTOR, "[role='table']")
    COLUMN_HEADERS = (By.CSS_SELECTOR, "[role='columnheader']")
    ROWS = (By.CSS_SELECTOR, "[role='row']")
    CELL = (By.CSS_SELECTOR, "[role='cell']")
    YELLOW_LABEL = (By.CLASS_NAME, "bg-warning")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout)

    def _get_table(self):
        return self._wait().until(EC.presence_of_element_located(self.TABLE))

    def _get_column_index(self, column_name: str) -> int:
        table = self._get_table()
        headers = table.find_elements(*self.COLUMN_HEADERS)
        for i, header in enumerate(headers):
            if header.text.strip() == column_name:
                return i
        raise ValueError(f"Column '{column_name}' not found in table")

    def get_cell_value(self, row_name: str, column_name: str) -> str:
        """Get a cell value by row identifier and column header name."""
        table = self._get_table()
        col_index = self._get_column_index(column_name)
        rows = table.find_elements(*self.ROWS)
        for row in rows:
            cells = row.find_elements(*self.CELL)
            if cells and row_name in cells[0].text.strip():
                return cells[col_index].text.strip()
        raise ValueError(f"Row '{row_name}' not found in table")

    def get_yellow_label_text(self) -> str:
        label = self._wait().until(EC.presence_of_element_located(self.YELLOW_LABEL))
        return label.text.strip()