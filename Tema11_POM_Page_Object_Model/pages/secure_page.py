"""
c. Secure page https://the-internet.herokuapp.com/secure
- Sa contina mesajul de succes si verificare ca e displayed
- Sa contina logout_btn si click pe el
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Tema11_POM_Page_Object_Model.pages.home_page import HomePage


class SecureArea(HomePage):

    SECURE_AREA_URL = 'https://the-internet.herokuapp.com/secure'
    LOGOUT_BTN = (By.CLASS_NAME, 'icon-signout')
    FLASH_MESSEGE = (By.CLASS_NAME, 'close')

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def click_on_logout_button(self):
        self.click(self.LOGOUT_BTN)

    def close_message(self):
        self.click(self.FLASH_MESSEGE)

    def get_element_text(self, locator):
        return self.find(locator).text

    def get_success_message_text(self):
        return self.get_success_message_text()

    def wait_for_element_to_be_present(self, element_locator, time):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(element_locator))

    def is_message_displayed(self):
        return self.wait_for_element_to_be_present(self.FLASH_MESSEGE, 5)

    def wait_for_element_to_be_absent(self, element_locator, time):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.none_of(EC.presence_of_element_located(element_locator)))

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def wait_for_message_to_be_absent(self):
        self.wait_for_element_to_be_absent(self.FLASH_MESSEGE, 5)

    def is_message_present(self):
        return self.is_element_present(self.FLASH_MESSEGE)

