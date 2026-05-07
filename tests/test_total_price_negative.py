import time
from pages.product_total_page import ProductTotalPage

#if product is out of stock checkout button wont work
def test_out_of_stock_checkout_should_be_blocked(driver):

    product = ProductTotalPage(driver)

    # ---------- STEP 1: Open Phones ----------
    product.open_phones_category()
    time.sleep(2)

    product.open_iphone()
    time.sleep(2)

    # ---------- STEP 2: Set HIGH qty ----------
    product.set_quantity(8)
    time.sleep(2)

    product.add_to_cart()
    time.sleep(3)

    # ---------- STEP 3: Go to Cart ----------
    product.open_cart_dropdown()
    time.sleep(2)

    product.click_view_cart()
    time.sleep(3)

    # ---------- STEP 4: Validate invalid product exists ----------
    assert "***" in driver.page_source

    # ---------- STEP 5: Try checkout ----------
    checkout_btn = driver.find_element(
        "xpath",
        "//a[contains(text(),'Checkout')]"
    )
    checkout_btn.click()

    time.sleep(2)

#check for invalid quantity 1000000
def test_invalid_cart_should_not_update_total(driver):
    product = ProductTotalPage(driver)

    product.open_phones_category()
    product.open_iphone()

    product.set_quantity(10000)  # invalid qty
    product.add_to_cart()

    product.open_cart_dropdown()
    product.click_view_cart()


    # NEGATIVE CHECK:
    # system should not allow invalid rows OR should flag error
    assert "***" in driver.page_source


#empty cart or 0
def test_empty_cart_should_block_checkout(driver):
    product = ProductTotalPage(driver)

    product.open_cart_dropdown()
    time.sleep(3)

    # NEGATIVE ASSERTION
    assert "Your shopping cart is empty" in driver.page_source


#edge cases

#negative value so empty cart
def test_negative_quantity_should_be_rejected(driver):
    product = ProductTotalPage(driver)

    product.open_phones_category()
    product.open_iphone()

    product.set_quantity(-5)
    product.add_to_cart()

    product.open_cart_dropdown()

    assert "Your shopping cart is empty" in driver.page_source