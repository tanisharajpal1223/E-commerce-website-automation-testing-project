import time
from pages.product_total_page import ProductTotalPage


def test_validate_total_price(driver):

    product = ProductTotalPage(driver)

    # ---------- STEP 1: Open Phones ----------
    product.open_phones_category()
    time.sleep(2)

    product.open_iphone()
    time.sleep(2)

    # ---------- STEP 2: Set qty = 2 ----------
    product.set_quantity(2)
    time.sleep(2)

    product.add_to_cart()
    time.sleep(3)

    # ---------- STEP 3: Go to Tablets ----------
    product.open_tablets_category()
    time.sleep(2)

    product.open_samsung_tab()
    time.sleep(2)

    # qty = 1 (default)
    product.add_to_cart()
    time.sleep(3)

    # ---------- STEP 4: Go to Cart ----------
    product.open_cart_dropdown()
    time.sleep(2)

    product.click_view_cart()
    time.sleep(3)

    # ---------- STEP 5: VALIDATION ----------
    product.validate_each_product_total()
    product.validate_final_total()