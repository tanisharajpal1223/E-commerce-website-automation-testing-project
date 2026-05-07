from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    # ---------- Locators ----------
    PHONES_MENU = (By.LINK_TEXT, "Phones & PDAs")
    IPHONE_LINK = (By.LINK_TEXT, "iPhone")

    IMAGE_THUMB = (By.XPATH, "//ul[@class='thumbnails']/li[1]")
    NEXT_BTN = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    CLOSE_BTN = (By.XPATH, "//button[@title='Close (Esc)']")

    ADD_TO_CART = (By.ID, "button-cart")
    QUANTITY = (By.ID, "input-quantity")

    # for price and total logic

    # for price and total logic

    PRODUCT_PRICE = (By.XPATH, "//h2")

    CART_TOTAL = (By.ID, "cart-total")
    VIEW_CART = (By.XPATH, '//p[@class="text-right"]/a[1]')

    # ---------- Cart Locators ----------
    CART_ROW = (By.XPATH, "//table//tbody/tr")
    CART_QTY = (By.XPATH, ".//input[contains(@name,'quantity')]")
    UNIT_PRICE = (By.XPATH, ".//td[5]")
    LINE_TOTAL = (By.XPATH, ".//td[6]")
    FINAL_TOTAL = (By.XPATH, "//strong[text()='Total']/parent::td/following-sibling::td")


    # for laptop and calendar functionality
    # ---------- Locators ----------

    LAPTOPS_MENU = (By.LINK_TEXT, "Laptops & Notebooks")

    # More reliable than text (because of spacing issue)
    SHOW_ALL_LAPTOPS = (By.CSS_SELECTOR, "a.see-all")

    HP_PRODUCT = (By.LINK_TEXT, "HP LP3065")

    # ---------- Calendar Locators ----------
    CALENDAR_ICON = (By.XPATH, '//i[@class="fa fa-calendar"]')
    NEXT_MONTH = (By.XPATH, '//th[@class="next"]')
    PREV_MONTH = (By.XPATH, '//th[@class="prev"]')
    MONTH_YEAR = (By.XPATH, '//th[@class="picker-switch"]')


    # ---------- Actions ----------
    def open_phones_category(self):
        self.click(self.PHONES_MENU)

    def open_iphone(self):
        self.click(self.IPHONE_LINK)

    def open_first_image(self):
        self.click(self.IMAGE_THUMB)

    def next_image(self):
        self.click(self.NEXT_BTN)

    def close_image(self):
        self.click(self.CLOSE_BTN)

    def set_quantity(self, qty):
        element = self.wait.until(
            lambda d: d.find_element(*self.QUANTITY)
        )
        element.click()
        element.clear()
        element.send_keys(str(qty))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    # ---------- Price & Cart Logic ----------

        # ---------- Price ----------
    def get_product_price(self):
        text = self.get_text(self.PRODUCT_PRICE)
        return float(text.replace("$", ""))

        # ---------- Navigation ----------

    def open_cart_dropdown(self):
        self.click(self.CART_TOTAL)

    def click_view_cart(self):
        self.click(self.VIEW_CART)

    def get_cart_quantity(self):
        row = self.driver.find_element(*self.CART_ROW)
        return int(row.find_element(*self.CART_QTY).get_attribute("value"))

    def get_line_total(self):
        row = self.driver.find_element(*self.CART_ROW)
        text = row.find_element(*self.LINE_TOTAL).text
        return float(text.replace("$", ""))

    def get_final_total(self):
        text = self.get_text(self.FINAL_TOTAL)
        return float(text.replace("$", ""))


    # actions for calendar and laptop functionality

        # ---------- Actions ----------

    def open_hp_product(self):
        # Step 1: Click menu
        self.click(self.LAPTOPS_MENU)

        # Step 2: Force click Show All (bypass visibility) opens on hover (CSS-based)
        # submenu is NOT interactable via click alone
        element = self.driver.find_element(*self.SHOW_ALL_LAPTOPS)
        self.driver.execute_script("arguments[0].click();", element)

        # Step 3: Click HP
        hp = self.driver.find_element(*self.HP_PRODUCT)
        hp.location_once_scrolled_into_view
        hp.click()

    def select_delivery_date(self, day, month, year):
        # open calendar
        self.driver.find_element(*self.CALENDAR_ICON).click()

        next_btn = self.driver.find_element(*self.NEXT_MONTH)
        month_year = self.driver.find_element(*self.MONTH_YEAR)

        target = f"{month} {year}"

        # move until correct month-year appears
        while month_year.text != target:
            next_btn.click()

        # select day
        self.driver.find_element(
            By.XPATH, f'//td[text()="{day}"]'
        ).click()