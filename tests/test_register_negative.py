import time

from pages.home_page import HomePage
from pages.register_page import RegisterPage

def test_duplicate_email(driver):

    home = HomePage(driver)
    home.go_to_register_page()

    register = RegisterPage(driver)

    register.enter_first_name("John")
    register.enter_last_name("Doe")
    register.enter_email("abcdef2332@gmail.com")  # already used
    register.enter_telephone("9876543210")
    register.enter_password("Test@123")
    register.enter_confirm_password("Test@123")

    register.select_newsletter_yes()
    register.accept_privacy()
    register.click_continue()

    assert "E-Mail Address is already registered" in driver.page_source



def test_missing_required_fields(driver):

    home = HomePage(driver)
    home.go_to_register_page()

    register = RegisterPage(driver)

    register.click_continue()

    assert "First Name must be between" in driver.page_source


