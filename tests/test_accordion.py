import pytest
import allure
from pages.main_page import MainPage
from data import accordion_data

class TestAccordion:
    @pytest.mark.parametrize("index, expected_text", accordion_data.ANSWERS)
    @allure.title("Проверка выпадающего списка в 'Вопросы о важном'")
    def test_accordion_text(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_question(index)
        assert main_page.get_answer_text(index) == expected_text
