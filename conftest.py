import pytest
from selenium import webdriver


# Marked the method as fixture for prerequisite and teardown method
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    print("Browser closed successfully")
