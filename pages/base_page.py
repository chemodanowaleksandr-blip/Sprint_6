from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """Открыть указанный URL в браузере"""
        self.driver.get(url)

    def find_element(self, locator, time=10):
        """Найти элемент с ожиданием его появления"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Not found {locator}"
        )

    def click_element(self, locator):
        """Кликнуть на элемент"""
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        """Проскроллить страницу до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments.scrollIntoView();", element)

    def get_text(self, locator):
        """Получить текст из элемента"""
        return self.find_element(locator).text

    def switch_to_new_window(self):
        """Переключиться на последнюю открытую вкладку (для логотипа Яндекса)"""
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):
        """Получить текущий URL адрес"""
        return self.driver.current_url
