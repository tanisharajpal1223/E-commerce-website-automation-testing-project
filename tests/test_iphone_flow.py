import time
import random

from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_iphone_image_and_add_to_cart(driver):

    home = HomePage(driver)
    product = ProductPage(driver)

    # ---------- STEP 1: Navigate ----------
    product.open_phones_category()
    time.sleep(2)

    product.open_iphone()
    time.sleep(2)

    # ---------- VALIDATION ----------
    assert "iPhone" in driver.title
    time.sleep(2)

    # ---------- STEP 2: Image gallery ----------
    product.open_first_image()
    time.sleep(2)

    for _ in range(6):
        product.next_image()
        time.sleep(2)

    # ---------- Screenshot ----------
    driver.save_screenshot(
        "screenshot_" + str(random.randint(0, 101)) + ".png"
    )
    time.sleep(2)

    # ---------- Close image ----------
    product.close_image()
    time.sleep(2)

    # ---------- STEP 3: Quantity handling (IMPORTANT FIX) ----------
    quantity = product.driver.find_element("id", "input-quantity")
    quantity.click()
    time.sleep(1)

    quantity.clear()
    time.sleep(1)

    quantity.send_keys("2")
    time.sleep(2)

    # ---------- STEP 4: Add to cart ----------
    product.add_to_cart()
    time.sleep(3)

    # ---------- VALIDATION ----------
    assert "Success" in driver.page_source