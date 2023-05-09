from time import sleep
from unittest import TestCase

from Tema11_POM_Page_Object_Model.pages.login_page import LoginPage
from Tema11_POM_Page_Object_Model.pages.secure_page import SecureArea
from Tema11_POM_Page_Object_Model.utils.driver_factory import DriverFactory


class TestSecureArea(TestCase):
    DEFAULT_USERNAME = 'tomsmith'
    DEFAULT_PASSWORD = 'SuperSecretPassword!'
    SUCCESS_LOGIN_MESSAGE = 'You logged into a secure area!'
    SUCCESS_LOGOUT_MESSAGE = 'You logged out of the secure area!'

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_login_page()
        login_page.username_type(self.DEFAULT_USERNAME)
        login_page.password_type(self.DEFAULT_PASSWORD)
        login_page.login()
        sleep(5)
        self.assertTrue(login_page.get_message_text(), 'Error, invalid text message!')

    def test_logout(self):
        self.test_login()
        login_page = LoginPage(self.driver)
        secure_page = SecureArea(self.driver)
        secure_page.click_on_logout_button()
        sleep(3)
        self.assertTrue(login_page.get_message_text(), 'Error, invalid text message!')

    def test_close_flash_message(self):
        self.test_login()
        sleep(3)
        secure_page = SecureArea(self.driver)
        secure_page.close_message()
        secure_page.wait_for_message_to_be_absent()
        assert not secure_page.is_message_present(), "Error, message is still displayed"


