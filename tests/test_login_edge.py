import time
from pages.home_page import HomePage
from pages.login_page import LoginPage





def test_email_with_spaces(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("   wrong@gmail.com   ")
    login.enter_password("wrong123")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()




def test_password_spaces_only(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("wrong@gmail.com")
    login.enter_password("     ")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()



def test_very_long_email(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    long_email = "a" * 300 + "@gmail.com"

    login.enter_email(long_email)
    login.enter_password("wrong123")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()



def test_sql_injection_email(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("' OR 1=1 --")
    login.enter_password("wrong123")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()



def test_special_characters_email(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("!!!@@@###$$$")
    login.enter_password("wrong123")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()



def test_numeric_email(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("1234567890")
    login.enter_password("wrong123")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()



def test_both_fields_empty(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("")
    login.enter_password("")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()