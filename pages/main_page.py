import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import urls  # Импортируем наш файл с урлами

class MainPage(BasePage):
    URL = urls.MAIN_PAGE_URL 

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        # Используем метод из BasePage вместо self.driver.get
        self.open_url(self.URL) 

    @allure.step("Принять куки, если они появились")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Кликнуть верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликнуть на вопрос номер {index}")
    def click_question(self, index):
        locator = MainPageLocators.get_question_locator(index)
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Получить текст ответа номер {index}")
    def get_answer_text(self, index):
        locator = MainPageLocators.get_answer_locator(index)
        return self.get_text(locator)

    @allure.step("Кликнуть на логотип Самоката")
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_logo_yandex(self):
        # ИСПРАВЛЕНО: Заменена точка на нижнее подчёркивание в названии локатора
        self.click_element(MainPageLocators.LOGO_YANDEX) 
