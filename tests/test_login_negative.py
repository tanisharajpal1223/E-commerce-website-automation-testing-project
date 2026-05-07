import time
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_invalid_login(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    time.sleep(2)  # ⏳ wait for page load

    login = LoginPage(driver)

    login.enter_email("wrong@gmail.com")
    time.sleep(1)

    login.enter_password("wrong123")
    time.sleep(1)

    login.click_login()

    time.sleep(2)  # ⏳ wait for error message

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()


def test_empty_login(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("")
    login.enter_password("")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()


def test_empty_email(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("")
    login.enter_password("wrong123")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()


def test_empty_password(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("wrong@gmail.com")
    login.enter_password("")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()


def test_invalid_email_format(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("abc123")   # invalid format
    login.enter_password("wrong123")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()


def test_wrong_password(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)

    login.enter_email("valid@email.com")   # replace with real registered email
    login.enter_password("wrongpass")
    login.click_login()

    assert "Warning: No match for E-Mail Address and/or Password." in login.get_warning_message()