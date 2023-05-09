"""
b. Login page https://the-internet.herokuapp.com/login
- Sa contina user, pass, login_btn si metode pt interactiune cu ele
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from Tema11_POM_Page_Object_Model.pages.home_page import HomePage


class LoginPage(HomePage):
    USER = (By.ID, 'username')
    PASS = (By.ID, 'password')
    LOGIN_BTN = (By.CLASS_NAME, 'fa-sign-in')
    LOGIN_MESSAGE = (By.ID, 'flash')

    LOGIN_PAGE_URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def username_type(self, username):
        self.type(self.USER, username)

    def password_type(self, password):
        self.type(self.PASS, password)

    def login(self):
        return self.click(self.LOGIN_BTN)

    def get_element_text(self, locator):
        return self.find(locator).text

    def get_message_text(self):
        return self.get_element_text(self.LOGIN_MESSAGE)

