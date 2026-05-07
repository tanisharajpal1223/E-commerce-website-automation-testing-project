from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    # ---------- Locators ----------
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")

    LOGIN_BTN = (By.XPATH, "//input[@value='Login']")
    FORGOT_PASSWORD = (By.LINK_TEXT, "Forgotten Password")

    WARNING_MSG = (By.CSS_SELECTOR, "div.alert-danger")

    # ---------- Actions ----------

    def enter_email(self, value):
        self.type(self.EMAIL, value)

    def enter_password(self, value):
        self.type(self.PASSWORD, value)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)

    def get_warning_message(self):
        return self.get_text(self.WARNING_MSG)






