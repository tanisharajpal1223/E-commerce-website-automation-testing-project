from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):

    # ---------- Locators ----------
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")

    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")

    NEWSLETTER_YES = (By.XPATH, "//input[@name='newsletter' and @value='1']")
    NEWSLETTER_NO  = (By.XPATH, "//input[@name='newsletter' and @value='0']")

    AGREE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BTN = (By.XPATH, "//input[@value='Continue']")

    SUCCESS_MSG = (By.TAG_NAME, "h1")

    # ---------- Actions ----------

    def enter_first_name(self, value):
        self.type(self.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.type(self.LAST_NAME, value)

    def enter_email(self, value):
        self.type(self.EMAIL, value)

    def enter_telephone(self, value):
        self.type(self.TELEPHONE, value)

    def enter_password(self, value):
        self.type(self.PASSWORD, value)

    def enter_confirm_password(self, value):
        self.type(self.CONFIRM_PASSWORD, value)

    def select_newsletter_yes(self):
        self.click(self.NEWSLETTER_YES)

    def select_newsletter_no(self):
        self.click(self.NEWSLETTER_NO)

    def accept_privacy(self):
        self.click(self.AGREE_CHECKBOX)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)