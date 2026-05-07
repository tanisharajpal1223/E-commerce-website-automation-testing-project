from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SuccessPage(BasePage):

    # ---------- Locators ----------
    SUCCESS_HEADER = (By.XPATH, "//h1[contains(text(),'Your Account Has Been Created')]")
    SUCCESS_TEXT = (By.XPATH, "//p[contains(text(),'Congratulations')]")
    CONTINUE_BTN = (By.LINK_TEXT, "Continue")

    # ---------- Actions ----------

    def get_success_header(self):
        return self.get_text(self.SUCCESS_HEADER)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_TEXT)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)