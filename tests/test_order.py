import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    ORDER_DATA = [
        ("Иван", "Иванов", "Москва, ул. Ленина 1", "Чистые пруды", "89091112233", "25.12.2026", "сутки", "black", "Позвонить за час"),
        ("Петр", "Петров", "Москва, ул. Мира 10", "Сокольники", "89994445566", "26.12.2026", "двое суток", "grey", "Оставить у двери")
    ]

    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment", ORDER_DATA)
    @allure.title("Позитивный флоу заказа самоката через ВЕРХНЮЮ кнопку")
    def test_order_via_top_button(self, driver, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page.fill_first_step(name, surname, address, metro, phone)
        order_page.fill_second_step(date, period, color, comment)
        assert order_page.is_order_created()

    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment", ORDER_DATA)
    @allure.title("Позитивный флоу заказа самоката через НИЖНЮЮ кнопку")
    def test_order_via_bottom_button(self, driver, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()

        order_page.fill_first_step(name, surname, address, metro, phone)
        order_page.fill_second_step(date, period, color, comment)
        assert order_page.is_order_created()

    @allure.title("Клик на логотип Самоката возвращает на главную страницу")
    def test_logo_scooter_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()
        
        main_page.click_logo_scooter()
        assert main_page.get_current_url() == main_page.URL

    @allure.title("Клик на логотип Яндекса открывает Дзен в новом окне")
    def test_logo_yandex_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        main_page.click_logo_yandex()
        main_page.switch_to_new_window()
        assert "dzen.ru" in main_page.get_current_url()
