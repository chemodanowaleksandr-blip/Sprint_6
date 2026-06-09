from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Not found {locator}"
        )

    def click_element(self, locator):
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments.scrollIntoView();", element)

    def get_text(self, locator):
        return self.find_element(locator).text
