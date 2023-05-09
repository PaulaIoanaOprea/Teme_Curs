"""
Avand ca exemplu pagina https://the-internet.herokuapp.com/login
Impementati 3 pagini intr-un nou proiect POM
a. Home page https://the-internet.herokuapp.com/
- Sa aiba cel putin 3 elemente inlcusiv Form Authentication
- Sa contina metode de click pe ele

"""

from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    HOME_URL = 'https://the-internet.herokuapp.com/'
    FORM_AUTHENTICATION = (By.LINK_TEXT,'Form Authentication')
    CONTEXT_MENU = (By.LINK_TEXT, 'Context Menu')
    FORGOT_PASSWORD = (By.LINK_TEXT,'E-mail')

    def go_to_home_page(self):
        self.driver.get(self.HOME_URL)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def click_to_form_authentication(self):
        return self.click(self.FORM_AUTHENTICATION)

    def click_to_context_menu(self):
        return self.click(self.CONTEXT_MENU)

    def click_to_forgot_password(self):
        return self.click(self.FORGOT_PASSWORD)
