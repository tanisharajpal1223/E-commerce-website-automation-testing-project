import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.success_page import SuccessPage
from Utils.logger import get_logger
from Utils.data_generator import generate_email 
from Utils.excel_reader import get_test_data
logger = get_logger()



test_data = get_test_data("testdata/registration.xlsx", "Sheet1")

@pytest.mark.parametrize("data", test_data)
def test_valid_registration(driver, data):

    email = generate_email()   # 👈 dynamic email

    logger.info("Starting test for user: %s", email)

    home = HomePage(driver)
    home.go_to_register_page()

    register = RegisterPage(driver)

    register.enter_first_name(data["first_name"])
    register.enter_last_name(data["last_name"])
    register.enter_email(email)
    register.enter_telephone(data["telephone"])

    register.enter_password(data["password"])
    register.enter_confirm_password(data["password"])

    register.select_newsletter_yes()
    register.accept_privacy()

    logger.info("Submitting form")
    register.click_continue()

    success = SuccessPage(driver)

    logger.info("Validating success message")

    assert success.get_success_header() == "Your Account Has Been Created!"

    logger.info("Test passed for user: %s", email)