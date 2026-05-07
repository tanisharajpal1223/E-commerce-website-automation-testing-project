import time
from selenium.webdriver.common.by import By

from pages.logout_page import LogoutPage
from pages.product_page import ProductPage
from pages.checkout_loginflow_page import CheckoutLoginflowPage


def test_login_and_buy_product(driver):

    logout = LogoutPage(driver)
    product = ProductPage(driver)
    checkout = CheckoutLoginflowPage(driver)

    # LOGIN
    logout.click_my_account()
    logout.click_login_link()

    logout.enter_email("wg344@gmail.com")
    logout.enter_password("2332")
    logout.click_login_button()

    driver.find_element(By.CSS_SELECTOR, "a[href*='common/home']").click()

    # PRODUCT
    product.open_hp_product()
    product.select_delivery_date(31, "December", 2012)

    qty = product.driver.find_element("id", "input-quantity")
    qty.clear()
    qty.send_keys("2")

    product.add_to_cart()

    # CHECKOUT
    checkout.open_cart()
    checkout.click_checkout()

    # SIMPLE FLOW (NO ADDRESS)
    checkout.quick_checkout_flow()


