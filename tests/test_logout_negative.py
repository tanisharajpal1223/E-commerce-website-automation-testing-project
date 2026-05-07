
from pages.logout_page import LogoutPage

#Logout should NOT be visible when user is NOT logged in
def test_logout_link_absence_when_guest(driver):

    logout = LogoutPage(driver)

    logout.click_my_account()

    logout_links = driver.find_elements(*logout.LOGOUT_LINK)

    assert len(logout_links) == 0