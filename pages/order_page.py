import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнить первую часть формы заказа")
    def fill_first_step(self, name, surname, address, metro, phone):
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.find_element(OrderPageLocators.METRO_INPUT).send_keys(metro)
        self.click_element(OrderPageLocators.METRO_OPTION)
        
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую часть формы заказа")
    def fill_second_step(self, date, period, color_id, comment):
        self.find_element(OrderPageLocators.DATE_INPUT).send_keys(date)
        self.click_element(OrderPageLocators.DATE_HEADER) # Закрыть календарь, чтобы не перекрывал кнопки
        
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.get_period_option_locator(period))
        
        self.click_element(OrderPageLocators.get_color_locator(color_id))
        self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить появление окна об успешном заказе")
    def is_order_created(self):
        return "Заказ оформлен" in self.get_text(OrderPageLocators.ORDER_CREATED_HEADER)
