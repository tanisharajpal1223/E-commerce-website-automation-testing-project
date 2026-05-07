import time


from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


def test_hp_product_add_to_cart(driver):

    home = HomePage(driver)
    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    # ---------- PRODUCT ----------
    product.open_hp_product()
    time.sleep(3)

    product.select_delivery_date(31, "December", 2012)


    quantity = product.driver.find_element("id", "input-quantity")
    quantity.clear()
    quantity.send_keys("2")

    product.add_to_cart()
    time.sleep(3)


    # ---------- CHECKOUT ----------
    checkout.open_cart()
    checkout.click_checkout()

    checkout.select_guest()
    checkout.continue_account()

    checkout.fill_billing()
    checkout.select_country_region()

    checkout.continue_guest_step2()
    checkout.continue_shipping()
    checkout.accept_terms()
    checkout.continue_payment()

    print("Final Price:", checkout.get_final_price())

    checkout.confirm_order()

    print("Success:", checkout.get_success_text())
