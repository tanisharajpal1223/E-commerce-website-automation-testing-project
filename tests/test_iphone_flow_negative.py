import time

from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_add_to_cart_invalid_quantity_cart_should_be_empty(driver):

    home = HomePage(driver)
    product = ProductPage(driver)

    product.open_phones_category()
    time.sleep(2)

    product.open_iphone()
    time.sleep(2)

    # ---------- invalid quantity ----------
    quantity = product.driver.find_element("id", "input-quantity")
    quantity.clear()
    time.sleep(1)

    quantity.send_keys("0")   # ❌ invalid value
    time.sleep(2)

    product.add_to_cart()
    time.sleep(3)

    # ---------- message check ----------
    assert "Success" in driver.page_source
    time.sleep(2)

    # ---------- cart validation ----------
    cart = driver.find_element("id", "cart-total").text
    time.sleep(2)

    print("Cart value:", cart)
    time.sleep(2)

    assert "0 item" in cart or "0.00" in cart
    time.sleep(2)


def test_add_to_cart_negative_quantity(driver):

    product = ProductPage(driver)

    product.open_phones_category()
    product.open_iphone()
    time.sleep(2)
    quantity = product.driver.find_element("id", "input-quantity")
    quantity.clear()
    quantity.send_keys("-5")
    time.sleep(2)
    product.add_to_cart()
    time.sleep(2)
    assert "Success" in driver.page_source
    time.sleep(2)


#edge case very large number
#System allows extreme quantity input causing integer overflow and incorrect cart calculation

def test_add_to_cart_large_quantity(driver):

    product = ProductPage(driver)
    time.sleep(2)
    product.open_phones_category()
    product.open_iphone()
    time.sleep(2)
    quantity = product.driver.find_element("id", "input-quantity")
    quantity.clear()
    quantity.send_keys("9999999999999999999999999999999999999999")
    time.sleep(2)
    product.add_to_cart()
    time.sleep(2)
    # system should handle limit or fail gracefully
    assert "Success" in driver.page_source or "error" in driver.page_source



#edge case rapid ultiple clicks

def test_multiple_click_add_to_cart(driver):

    product = ProductPage(driver)

    product.open_phones_category()
    product.open_iphone()

    for _ in range(10000):
        product.add_to_cart()
        time.sleep(1)

    # system should not break or duplicate incorrectly
    assert "Success" in driver.page_source