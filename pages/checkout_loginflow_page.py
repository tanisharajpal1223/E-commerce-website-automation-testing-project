from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutLoginflowPage(BasePage):

    # ===================== LOCATORS =====================
    CART_TOTAL = (By.ID, "cart-total")
    CHECKOUT_BTN = (By.LINK_TEXT, "Checkout")

    # Billing
    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    ADDRESS1 = (By.ID, "input-payment-address-1")
    CITY = (By.ID, "input-payment-city")
    POSTCODE = (By.ID, "input-payment-postcode")
    COUNTRY = (By.ID, "input-payment-country")
    REGION = (By.ID, "input-payment-zone")
    BILLING_CONTINUE = (By.ID, "button-payment-address")

    # Delivery address choice
    EXISTING_ADDRESS = (By.CSS_SELECTOR, "input[value='existing']")
    NEW_ADDRESS = (By.CSS_SELECTOR, "input[value='new']")
    DELIVERY_CONTINUE = (By.ID, "button-shipping-address")

    # Shipping / Payment
    SHIPPING_CONTINUE = (By.ID, "button-shipping-method")
    TERMS = (By.NAME, "agree")
    PAYMENT_CONTINUE = (By.ID, "button-payment-method")

    CONFIRM_ORDER = (By.ID, "button-confirm")
    SUCCESS = (By.TAG_NAME, "h1")

    # ===================== BASIC ACTIONS =====================

    def open_cart(self):
        self.click(self.CART_TOTAL)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    # ===================== SIMPLE FLOW =====================

    def quick_checkout_flow(self):

        # STEP 1: Billing → just CONTINUE
        self.click(self.BILLING_CONTINUE)

        # STEP 2: Delivery → CONTINUE
        self.click(self.DELIVERY_CONTINUE)

        # STEP 3: Shipping → CONTINUE
        self.click(self.SHIPPING_CONTINUE)

        # STEP 4: Terms → ACCEPT + CONTINUE
        self.click(self.TERMS)
        self.click(self.PAYMENT_CONTINUE)

        # STEP 5: CONFIRM ORDER
        self.click(self.CONFIRM_ORDER)

    # ===================== FINAL =====================

    def confirm_order(self):
        self.click(self.CONFIRM_ORDER)

    def get_success_message(self):
        return self.get_text(self.SUCCESS)