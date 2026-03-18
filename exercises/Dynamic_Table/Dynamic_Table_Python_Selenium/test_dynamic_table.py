from selenium.webdriver.remote.webdriver import WebDriver
from dynamic_table import DynamicTablePage

def test_compare_cpu_load(driver: WebDriver):
    table_page = DynamicTablePage(driver)

    driver.get("http://uitestingplayground.com/dynamictable")

    cpu_load_table = table_page.get_cell_value("Chrome", "CPU")
    cpu_load_banner = table_page.get_yellow_label_text()

    assert cpu_load_banner == f"Chrome CPU: {cpu_load_table}"