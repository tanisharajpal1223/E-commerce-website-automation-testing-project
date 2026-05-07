
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from Utils.login_reader import get_test_data
from Utils.logger import get_logger
from pages.forgot_password_page import ForgotPasswordPage

logger = get_logger()

# Load login data (already registered users)
test_data = get_test_data("testdata/login.xlsx", "Sheet1")


@pytest.mark.parametrize("data", test_data)
def test_valid_login(driver, data):

    logger.info("Starting login test for user: %s", data["email"])

    # ---------- Navigate ----------
    home = HomePage(driver)
    home.go_to_login_page()

    # ---------- Login Page ----------
    login = LoginPage(driver)

    # ---------- Enter credentials ----------
    login.enter_email(data["email"])
    login.enter_password(data["password"])

    # ---------- Submit ----------
    login.click_login()

    # ---------- Validation ----------
    assert "My Account" in driver.page_source

    logger.info("Login successful for user: %s", data["email"])



def test_forgot_password_any_email(driver):

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)
    login.click_forgot_password()

    forgot = ForgotPasswordPage(driver)

    forgot.enter_email("abcdef332@gmail.com")
    forgot.click_continue()

    assert "An email with a confirmation link has been sent your email address" in forgot.get_success_message()