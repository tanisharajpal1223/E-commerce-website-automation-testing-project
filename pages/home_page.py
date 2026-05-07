from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    # ---------- Locators ----------
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    LOGIN_LINK = (By.LINK_TEXT, "Login")

    # ---------- Actions ----------

    def open_my_account_menu(self):
        self.click(self.MY_ACCOUNT)



    def click_register(self):
        self.click(self.REGISTER_LINK)

    def click_login(self):  # ✅ ADD THIS
        self.click(self.LOGIN_LINK)

    def go_to_register_page(self):
        self.open_my_account_menu()
        self.click_register()

    def go_to_login_page(self):  # ✅ ADD THIS
        self.open_my_account_menu()
        self.click_login()

