from pages.logout_page import LogoutPage


def test_login_logout_flow(driver):

    logout = LogoutPage(driver)

    # ---------- STEP 1: My Account → Login ----------
    logout.click_my_account()
    logout.click_login_link()

    # ---------- STEP 2: LOGIN ----------
    logout.enter_email("abcdef332@gmail.com")
    logout.enter_password("Test@123")
    logout.click_login_button()

    assert "My Account" in driver.page_source

    # ---------- STEP 3: My Account → Logout ----------
    logout.click_my_account()
    logout.click_logout()


    # ---------- STEP 5: CONTINUE ----------
    logout.click_continue()




    



