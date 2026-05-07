from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # ---------- LOCATORS ----------
    CART_TOTAL = (By.ID, "cart-total")
    CHECKOUT_BTN = (By.XPATH, '//p[@class="text-right"]/a[2]')

    GUEST_RADIO = (By.XPATH, '//input[@value="guest"]')
    CONTINUE_ACCOUNT = (By.ID, "button-account")

    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    EMAIL = (By.ID, "input-payment-email")
    TELEPHONE = (By.ID, "input-payment-telephone")
    ADDRESS = (By.ID, "input-payment-address-1")
    CITY = (By.ID, "input-payment-city")
    POSTCODE = (By.ID, "input-payment-postcode")

    COUNTRY = (By.ID, "input-payment-country")
    REGION = (By.ID, "input-payment-zone")

    CONTINUE_GUEST = (By.ID, "button-guest")
    CONTINUE_SHIPPING = (By.ID, "button-shipping-method")
    AGREE_TERMS = (By.NAME, "agree")
    CONTINUE_PAYMENT = (By.ID, "button-payment-method")

    FINAL_PRICE = (By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
    CONFIRM_ORDER = (By.ID, "button-confirm")
    SUCCESS_TEXT = (By.XPATH, '//div[@class="col-sm-12"]/h1')

    # ---------- ACTIONS ----------

    def open_cart(self):
        self.click(self.CART_TOTAL)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def select_guest(self):
        self.click(self.GUEST_RADIO)

    def continue_account(self):
        self.click(self.CONTINUE_ACCOUNT)

    def fill_billing(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )

        self.driver.find_element(*self.FIRST_NAME).send_keys("test_first_name")
        self.driver.find_element(*self.LAST_NAME).send_keys("test_last_name")
        self.driver.find_element(*self.EMAIL).send_keys("test@test.com")
        self.driver.find_element(*self.TELEPHONE).send_keys("012345678")
        self.driver.find_element(*self.ADDRESS).send_keys("teststreet 187")
        self.driver.find_element(*self.CITY).send_keys("Frankfurt")
        self.driver.find_element(*self.POSTCODE).send_keys("112233")

    # ---------- FIXED COUNTRY + REGION ----------
    def select_country_region(self):
        # ---------- COUNTRY ----------
        country_el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COUNTRY)
        )
        country_el.click()

        country_select = Select(country_el)
        country_select.select_by_visible_text("India")  # change if needed

        # ---------- WAIT FOR REGION TO LOAD ----------
        WebDriverWait(self.driver, 10).until(
            lambda d: len(Select(d.find_element(*self.REGION)).options) > 1
        )

        # ---------- REGION ----------
        region_el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REGION)
        )
        region_el.click()

        region_select = Select(region_el)
        region_select.select_by_visible_text("Punjab")




    def continue_guest_step2(self):
        self.click(self.CONTINUE_GUEST)

    def continue_shipping(self):
        self.click(self.CONTINUE_SHIPPING)

    def accept_terms(self):
        self.click(self.AGREE_TERMS)

    def continue_payment(self):
        self.click(self.CONTINUE_PAYMENT)

    def get_final_price(self):
        return self.get_text(self.FINAL_PRICE)

    def confirm_order(self):
        self.click(self.CONFIRM_ORDER)

    def get_success_text(self):
        return self.get_text(self.SUCCESS_TEXT)