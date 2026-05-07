import pytest
import time

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

#Invalid Delivery Date (Future / Wrong Format)
def test_invalid_delivery_date(driver):

    product = ProductPage(driver)

    product.open_hp_product()
    time.sleep(2)

    # invalid date (future or not available)
    product.select_delivery_date(31, "December", 2050)

    quantity = product.driver.find_element("id", "input-quantity")
    quantity.clear()
    quantity.send_keys("1")

    product.add_to_cart()
    time.sleep(2)

    # validation (should NOT succeed)
    assert "Success" not in driver.page_source



def test_empty_quantity(driver):

    product = ProductPage(driver)

    product.open_hp_product()
    time.sleep(2)

    quantity = product.driver.find_element("id", "input-quantity")
    quantity.clear()   # empty

    product.add_to_cart()
    time.sleep(2)

    assert "Success" in driver.page_source



def test_checkout_without_guest_selection(driver):

    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    product.open_hp_product()
    product.select_delivery_date(31, "December", 2012)

    quantity = product.driver.find_element("id", "input-quantity")
    quantity.send_keys("1")

    product.add_to_cart()

    checkout.open_cart()
    checkout.click_checkout()

    # skip guest selection intentionally
    checkout.continue_account()

    assert "Warning" in driver.page_source or "Error" in driver.page_source




def test_missing_billing_details(driver):

    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    product.open_hp_product()
    product.select_delivery_date(31, "December", 2012)

    quantity = product.driver.find_element("id", "input-quantity")
    quantity.send_keys("1")

    product.add_to_cart()

    checkout.open_cart()
    checkout.click_checkout()

    checkout.select_guest()
    checkout.continue_account()

    # DO NOT fill billing details
    checkout.continue_guest_step2()




def test_invalid_country_region(driver):

    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    product.open_hp_product()
    product.select_delivery_date(31, "December", 2012)

    quantity = product.driver.find_element("id", "input-quantity")
    quantity.send_keys("1")

    product.add_to_cart()

    checkout.open_cart()
    checkout.click_checkout()

    checkout.select_guest()
    checkout.continue_account()

    checkout.fill_billing()

    # skip country/region intentionally
    checkout.continue_guest_step2()




def test_without_terms_acceptance(driver):

    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    product.open_hp_product()
    product.select_delivery_date(31, "December", 2012)

    quantity = product.driver.find_element("id", "input-quantity")
    quantity.send_keys("1")

    product.add_to_cart()

    checkout.open_cart()
    checkout.click_checkout()

    checkout.select_guest()
    checkout.continue_account()

    checkout.fill_billing()
    checkout.select_country_region()

    checkout.continue_guest_step2()
    checkout.continue_shipping()

    # skip terms acceptance
    checkout.continue_payment()




def test_invalid_email(driver):

    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    product.open_hp_product()
    product.select_delivery_date(31, "December", 2012)

    qty = product.driver.find_element("id", "input-quantity")
    qty.send_keys("1")

    product.add_to_cart()

    checkout.open_cart()
    checkout.click_checkout()

    checkout.select_guest()
    checkout.continue_account()

    checkout.fill_billing()

    # overwrite invalid email
    checkout.driver.find_element("id", "input-payment-email").clear()
    checkout.driver.find_element("id", "input-payment-email").send_keys("invalid-email")

    checkout.select_country_region()
    checkout.continue_guest_step2()




def test_missing_country(driver):

    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    product.open_hp_product()
    product.select_delivery_date(31, "December", 2012)

    qty = product.driver.find_element("id", "input-quantity")
    qty.send_keys("1")

    product.add_to_cart()

    checkout.open_cart()
    checkout.click_checkout()

    checkout.select_guest()
    checkout.continue_account()

    checkout.fill_billing()

    # ❌ skip country + region
    checkout.continue_guest_step2()









