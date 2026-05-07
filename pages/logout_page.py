from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LogoutPage(BasePage):

    # ---------- Locators ----------
    MY_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BTN = (By.XPATH, "//input[@value='Login']")

    LOGOUT_HEADER = (By.TAG_NAME, "h1")
    CONTINUE_BTN = (By.LINK_TEXT, "Continue")

    HOME_BTN = (By.CSS_SELECTOR, "a[href*='common/home']")


    # ---------- Actions ----------

    def click_my_account(self):
        self.click(self.MY_ACCOUNT)

    def click_login_link(self):
        self.click(self.LOGIN_LINK)

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login_button(self):
        self.click(self.LOGIN_BTN)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def get_logout_header(self):
        return self.get_text(self.LOGOUT_HEADER)













        def click_home(self):
            self.click(self.HOME_BTN)

