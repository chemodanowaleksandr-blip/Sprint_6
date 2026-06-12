import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    @pytest.mark.parametrize(
        "button_type, name, surname, address, metro, phone, date, period, color, comment",
        [
            ("top", "Иван", "Иванов", "Москва, ул. Ленина 1", "Чистые пруды", "89091112233", "25.12.2026", "сутки", "black", "Позвонить за час"),
            ("bottom", "Петр", "Петров", "Москва, ул. Мира 10", "Сокольники", "89994445566", "26.12.2026", "двое суток", "grey", "Оставить у двери")
        ]
    )
    @allure.title("Позитивный флоу заказа самоката и проверка переходов по лого")
    def test_order_flow_and_logos(self, driver, button_type, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()

        # Выбор точки входа (верхняя или нижняя кнопка)
        if button_type == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        # Оформление заказа (Шаг 1 и Шаг 2)
        order_page.fill_first_step(name, surname, address, metro, phone)
        order_page.fill_second_step(date, period, color, comment)

        # 1. Проверка создания заказа
        assert order_page.is_order_created()

        # 2. Проверка логотипа Самоката (возврат на главную)
        main_page.click_logo_scooter()
        assert main_page.get_current_url() == main_page.URL

        # 3. Проверка логотипа Яндекса (открытие Дзена в новом окне)
        main_page.click_logo_yandex()
        main_page.switch_to_new_window()
        assert "dzen.ru" in main_page.get_current_url()
