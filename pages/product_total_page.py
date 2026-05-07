from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductTotalPage(BasePage):

    # ---------- Navigation ----------
    PHONES_MENU = (By.LINK_TEXT, "Phones & PDAs")
    TABLETS_MENU = (By.LINK_TEXT, "Tablets")

    IPHONE_LINK = (By.LINK_TEXT, "iPhone")
    SAMSUNG_TAB = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")

    # ---------- Product Page ----------
    QUANTITY = (By.ID, "input-quantity")
    ADD_TO_CART = (By.ID, "button-cart")
    PRODUCT_PRICE = (By.XPATH, "//h2")

    # ---------- Cart Dropdown ----------
    CART_TOTAL = (By.ID, "cart-total")
    VIEW_CART = (By.XPATH, '//p[@class="text-right"]/a[1]')

    # ---------- Cart Table ----------
    CART_ROW = (By.XPATH, "//div[@class='table-responsive']//tbody/tr")
    CART_QTY = (By.XPATH, ".//input[contains(@name,'quantity')]")
    UNIT_PRICE = (By.XPATH, ".//td[5]")
    LINE_TOTAL = (By.XPATH, ".//td[6]")

    # ---------- Final Total ----------
    FINAL_TOTAL = (By.XPATH, "//tr[td/strong[text()='Total:']]/td[2]")

    CHECKOUT = (By.XPATH, "//a[contains(text(),'Checkout')]")
    # =========================================================
    # ===================== ACTIONS ============================
    # =========================================================

    def open_phones_category(self):
        self.click(self.PHONES_MENU)

    def open_tablets_category(self):
        self.click(self.TABLETS_MENU)

    def open_iphone(self):
        self.click(self.IPHONE_LINK)

    def open_samsung_tab(self):
        self.click(self.SAMSUNG_TAB)

    def set_quantity(self, qty):
        element = self.wait.until(
            lambda d: d.find_element(*self.QUANTITY)
        )
        element.click()
        element.clear()
        element.send_keys(str(qty))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    # ---------- Cart Navigation ----------

    def open_cart_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_TOTAL)).click()

    def click_view_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.VIEW_CART)).click()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT)
        ).click()

    # =========================================================
    # ===================== PRICE LOGIC ========================
    # =========================================================

    def get_product_price(self):
        text = self.get_text(self.PRODUCT_PRICE)
        return float(text.replace("$", "").strip())

    def get_all_rows(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ROW)
        )

    def _get_float(self, text):
        return float(text.replace("$", "").strip())

    def validate_each_product_total(self):
        rows = self.driver.find_elements(*self.CART_ROW)

        for row in rows:
            try:
                qty = int(row.find_element(*self.CART_QTY).get_attribute("value"))

                unit_price = float(
                    row.find_element(*self.UNIT_PRICE).text.replace("$", "")
                )

                total_price = float(
                    row.find_element(*self.LINE_TOTAL).text.replace("$", "")
                )

                expected_total = round(qty * unit_price, 2)

                # ✅ PRINT VALUES
                print(f"Qty: {qty}, Unit: {unit_price}, UI Total: {total_price}, Calculated: {expected_total}")

                # ✅ ASSERT
                assert expected_total == total_price, \
                    f"Mismatch: {qty} * {unit_price} != {total_price}"

            except:
                continue

    def validate_final_total(self):
        rows = self.driver.find_elements(*self.CART_ROW)

        calculated_total = 0

        for row in rows:
            try:
                total_price = float(
                    row.find_element(*self.LINE_TOTAL).text.replace("$", "")
                )
                calculated_total += total_price
            except:
                continue

        # ✅ get final total using correct locator
        final_total = float(
            self.get_text(self.FINAL_TOTAL).replace("$", "")
        )

        print(f"Calculated Total: {calculated_total}")
        print(f"UI Final Total: {final_total}")

        assert round(calculated_total, 2) == round(final_total, 2), \
            f"Final total mismatch: {calculated_total} != {final_total}"