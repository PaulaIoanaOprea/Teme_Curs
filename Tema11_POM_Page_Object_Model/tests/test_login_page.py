import unittest
from time import sleep

from Tema11_POM_Page_Object_Model.pages.login_page import LoginPage
from Tema11_POM_Page_Object_Model.pages.secure_page import SecureArea
from Tema11_POM_Page_Object_Model.utils.driver_factory import DriverFactory


class TestLoginPage(unittest.TestCase):
    DEFAULT_USERNAME = 'tomsmith'
    DEFAULT_PASSWORD = 'SuperSecretPassword!'
    NEW_USERNAME = 'opreapaulaioana'
    NEW_PASSWORD = 'Parolanoua123'

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_default_user_and_pass(self):
        login_page = LoginPage(self.driver)
        secure_page = SecureArea(self.driver)
        login_page.go_to_login_page()
        login_page.username_type(self.DEFAULT_USERNAME)
        login_page.password_type(self.DEFAULT_PASSWORD)
        login_page.login()
        login_page.get_message_text()
        sleep(5)
        self.assertTrue(secure_page.is_message_displayed(), "Error, message is not displayed")

    def test_login_with_new_user_and_pass(self):
        login_page = LoginPage(self.driver)
        secure_page = SecureArea(self.driver)
        login_page.go_to_login_page()
        login_page.username_type(self.NEW_USERNAME)
        login_page.password_type(self.NEW_PASSWORD)
        login_page.login()
        login_page.get_message_text()
        sleep(5)
        self.assertTrue(secure_page.is_message_displayed(), "Error, message is not displayed")

