"""
2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
"""

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


class TestAuthentication(unittest.TestCase):
    LINK = "https://auth.emag.ro/user/login"
    BUTON_LOGARE = (By.ID, 'user_login_continue')
    EMAIL_LOGARE = (By.ID, 'user_login_email')
    FB_LOGARE = (By.CLASS_NAME, 'facebook')
    GOOGLE_LOGARE = (By.CLASS_NAME, 'google')
    APPLE_LOGARE = (By.CLASS_NAME, 'apple')

    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def click_email_login(self):
        self.driver.find_element(*self.EMAIL_LOGARE).click()

    def click_fb_login(self):
        self.driver.find_element(*self.FB_LOGARE).click()

    def click_google_login(self):
        self.driver.find_element(*self.GOOGLE_LOGARE).click()

    def click_apple_login(self):
        self.driver.find_element(*self.APPLE_LOGARE).click()

    def is_element_present(self, element_locator):
        return len(self.driver.find_elements(*element_locator)) > 0

    def test_url(self):
        expected_url = 'https://auth.emag.ro/user/login'
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url), f'Invalid URL, expected {expected_url}, and found {actual_url}'

    def test_title(self):
        expected_title = "eMAG.ro - Libertate în fiecare zi"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title), f"Invalid title"

    def test_logo_displayed(self):
        logo = self.driver.find_element(By.CLASS_NAME, 'auth-logo')
        self.assertTrue(logo.is_displayed()), f"Logo not displayed"

    def test_buton_displayed(self):
        buton_submit = self.driver.find_element(*self.BUTON_LOGARE)
        assert buton_submit.is_displayed(), f' Buton Login neafisat!'

    def test_atribut_href(self):
        expected_href = "https://www.emag.ro/"
        actual_href = self.driver.find_element(By.CLASS_NAME, 'd-inline-block').get_attribute('href')
        self.assertEqual(expected_href,
                         actual_href), f"Invalid title, expected {expected_href}, but found {actual_href}"

    def test_eroare_displayed(self):
        self.click_email_login()
        camp_obligatoriu = self.driver.find_element(By.ID, 'user_login_email')
        assert camp_obligatoriu.is_displayed(), 'Eroarea nu este afisata fara user'

    def test_logare(self):
        user = self.driver.find_element(*self.EMAIL_LOGARE)
        user.send_keys('opreapaulaioana@gmail.com')
        self.click_email_login()
        expected_message = 'Your username is invalid!'
        actual_message = self.driver.find_element(By.ID, 'user_login_email').text
        self.assertTrue(expected_message, actual_message), 'Error message text is incorrect'

    def test_logare_fb(self):
        self.click_fb_login()
        expected_title = "Log into Facebook | Facebook"
        actual_title = self.driver.title
        self.assertEquals(expected_title, actual_title)

    def test_logare_google_cont_negasit(self):
        self.click_google_login()

        email_input = self.driver.find_element(By.ID, 'identifierId')
        email_input.send_keys('dumidupi@gmail.com')
        buton_inainte = self.driver.find_element(By.XPATH, "//span[text()='Înainte']")
        buton_inainte.click()

        eroare_cont_negasit = self.driver.find_element(By.XPATH, "//div[text()='Contul Google nu a fost găsit']")

        self.assertTrue(eroare_cont_negasit.is_displayed())

    def test_logare_apple_buton_prezent(self):
        self.click_apple_login()
        self.assertTrue(self.is_element_present((By.ID, 'sign-in')))


class TestDropdown(unittest.TestCase):
    LINK = 'https://www.emag.ro/'
    DROPDOWN = (By.XPATH, '/html/body/div[8]/div/ul')

    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_meniu(self):
        meniu = self.driver.find_element(*self.DROPDOWN)
        optiune = Select(meniu)  # nu inteleg de ce imi da eroare aici?

        index_selectat = '2'
        optiune.select_by_index(index_selectat)
        sleep(2)
        optiune_index = optiune.all_selected_options.index()
        assert optiune_index == "2"
