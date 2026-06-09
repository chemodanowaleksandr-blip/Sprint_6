import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Режим без экрана для работы в облаке GitHub
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
