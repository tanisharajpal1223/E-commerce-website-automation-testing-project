from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):

    EMAIL = (By.ID, "input-email")
    CONTINUE_BTN = (By.XPATH, "//input[@value='Continue']")

    SUCCESS_MSG = (By.CSS_SELECTOR, "div.alert.alert-success")

    def enter_email(self, value):
        self.type(self.EMAIL, value)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)