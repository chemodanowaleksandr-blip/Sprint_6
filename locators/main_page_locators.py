from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    BOTTOM_ORDER_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__39N7A")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__2gXMS")

    @staticmethod
    def get_question_locator(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def get_answer_locator(index):
        return (By.ID, f"accordion__panel-{index}")
