from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Шаг 1: Для кого самокат
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.CLASS_NAME, "Order_SelectOption__82W8f")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # Шаг 2: Про аренду
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE_HEADER = (By.CLASS_NAME, "Order_Header__21ftN")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1x12d']/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_CREATED_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @staticmethod
    def get_period_option_locator(period_text):
        return (By.XPATH, f".//div[@class='Dropdown-menu']/div[text()='{period_text}']")

    @staticmethod
    def get_color_locator(color_id):
        return (By.ID, color_id)
