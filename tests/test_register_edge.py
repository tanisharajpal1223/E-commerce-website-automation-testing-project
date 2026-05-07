from pages.home_page import HomePage
from pages.register_page import RegisterPage


#edge case on first name
def test_first_name_too_long(driver):

    home = HomePage(driver)
    home.go_to_register_page()

    register = RegisterPage(driver)

    long_name = "A" * 33  # 33 characters (invalid)

    register.enter_first_name(long_name)
    register.enter_last_name("Doe")
    register.enter_email("test12345@gmail.com")
    register.enter_telephone("9876543210")
    register.enter_password("Test@123")
    register.enter_confirm_password("Test@123")

    register.select_newsletter_yes()
    register.accept_privacy()
    register.click_continue()

    assert "First Name must be between" in driver.page_source




#edge case on password mismatch
def test_password_mismatch(driver):

    home = HomePage(driver)
    home.go_to_register_page()

    register = RegisterPage(driver)

    register.enter_first_name("John")
    register.enter_last_name("Doe")
    register.enter_email("john12345@gmail.com")  # use new email
    register.enter_telephone("9876543210")

    register.enter_password("Test@123")
    register.enter_confirm_password("Test@456")  # ❌ mismatch

    register.select_newsletter_yes()
    register.accept_privacy()
    register.click_continue()

    assert "Password confirmation does not match password!" in driver.page_source



#edge case on password too  short
def test_password_too_short(driver):

    home = HomePage(driver)
    home.go_to_register_page()

    register = RegisterPage(driver)

    register.enter_first_name("John")
    register.enter_last_name("Doe")
    register.enter_email("johnshort123@gmail.com")  # new email
    register.enter_telephone("9876543210")

    register.enter_password("123")   # ❌ less than 4 chars
    register.enter_confirm_password("123")

    register.select_newsletter_yes()
    register.accept_privacy()
    register.click_continue()

    assert "Password must be between 4 and 20 characters!" in driver.page_source


#telephone too short
def test_telephone_too_short(driver):

    home = HomePage(driver)
    home.go_to_register_page()

    register = RegisterPage(driver)

    register.enter_first_name("John")
    register.enter_last_name("Doe")
    register.enter_email("johnphone123@gmail.com")  # new email
    register.enter_telephone("12")   # ❌ less than 3 chars

    register.enter_password("Test@123")
    register.enter_confirm_password("Test@123")

    register.select_newsletter_yes()
    register.accept_privacy()
    register.click_continue()

    assert "Telephone must be between 3 and 32 characters!" in driver.page_source