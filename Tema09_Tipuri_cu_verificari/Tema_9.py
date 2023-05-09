import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
"""


class Login(TestCase):
    driver = None
    LINK = 'https://the-internet.herokuapp.com/login'
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    BUTON_LOGARE = (By.CLASS_NAME, 'fa-sign-in')
    SECURE_AREA = (By.XPATH, "//div[@class='flash success']")
    ERROR_MESSAGE = (By.ID, "flash")
    ERROR_CLOSE = (By.CLASS_NAME, "close")

    def setUp(self):  # ruleaza inainte de fiecare test
        print(f'Se executa setUp-ul pentru {self._testMethodName}')
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(1)

    def tear_Down(self):  # ruleaza dupa fiecare test
        print(f'Se executa tearDown-ul pentru {self._testMethodName}\n')
        self.driver.quit()

    def wait(self, element_locator, timp):
        wait = WebDriverWait(self.driver, timp)
        return wait.until(EC.presence_of_element_located(element_locator))

    def logare(self):
        self.driver.find_element(*self.BUTON_LOGARE).click()

    # ● Test 1
    # - Verifică dacă noul url e corect

    def test_url(self):
        print(f'A inceput testul {self._testMethodName}')
        url_1 = 'https://the-internet.herokuapp.com/login'
        url_2 = self.driver.current_url
        assert url_1 == url_2, f'Invalid URL, expected {url_1}, and found {url_2}'

    # ● Test 2
    # - Verifică dacă page title e corect

    def test_titlu(self):
        print(f'A inceput testul {self._testMethodName}')
        titlu_1 = 'The Internet'
        titlu_2 = self.driver.title
        assert titlu_1 == titlu_2, f"Invalid title, expected {titlu_1}, but found {titlu_2}"

    # ● Test 3
    # - Verifică textul de pe elementul xpath=//h2 e corect

    def test_text(self):
        print(f'A inceput testul {self._testMethodName}')
        element_actual = self.driver.find_element(By.XPATH, "//h2").text
        element_asteptat = 'Login Page'
        assert element_asteptat == element_actual, f'Invalid message \n Expected {element_asteptat} but found {element_actual}'

    # ● Test 4
    # - Verifică dacă butonul de login este displayed

    def test_buton_login_displayed(self):
        print(f'A inceput testul {self._testMethodName}')

        login_button = self.driver.find_element(*self.BUTON_LOGARE)
        assert login_button.is_displayed(), f' Buton Login neafisat!'

    # ● Test 5
    # - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_atribut_hrief(self):
        print(f'A inceput testul {self._testMethodName}')
        atribut_href_1 = "http://elementalselenium.com/"
        atribut_href_2 = self.driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute('href')
        assert atribut_href_1 == atribut_href_2, f"Invalid title, expected {atribut_href_1}, but found {atribut_href_2}"

    # ● Test 6
    # - Lasă goale user și pass
    # - Click login
    # - Verifică dacă eroarea e displayed

    def test_eroare_displayed(self):
        print(f'A inceput testul {self._testMethodName}')
        self.logare()
        eroare = self.driver.find_element(By.ID, 'flash')
        assert eroare.is_displayed(), 'Eroarea nu este afisata fara user si pass'

    # ● Test 7
    # - Completează cu user și pass invalide
    # - Click login
    # - Verifică dacă mesajul de pe eroare e corect
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    # expected = 'Your username is invalid!'
    # self.assertTrue(expected in actual, 'Error message text is
    # incorrect')

    def test_message_text(self):
        print(f'A inceput testul {self._testMethodName}')
        user = self.driver.find_element(*self.USERNAME)
        user.send_keys('Oprea_Paula')
        parola = self.driver.find_element(*self.PASSWORD)
        parola.send_keys('invalidpass')
        self.logare()
        expected_message = 'Your username is invalid!'
        actual_message = self.driver.find_element(By.ID, 'flash').text
        self.assertTrue(expected_message in actual_message), 'Error message text is incorrect'

    # ● Test 8
    # - Lasă goale user și pass
    # - Click login
    # - Apasă x la eroare
    # - Verifică dacă eroarea a dispărut

    def is_element_present(self, element_locator):
        return len(self.driver.find_elements(*element_locator)) > 0

    def wait_for_element_to_be_absent(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.none_of(EC.presence_of_element_located(element_locator)))

    def test_delete_error(self):
        self.driver.find_element(*self.BUTON_LOGARE).click()
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(error.is_displayed(), "Error message is not displayed")

        self.driver.find_element(*self.ERROR_CLOSE).click()
        self.wait_for_element_to_be_absent(self.ERROR_MESSAGE, 2)

        assert not self.is_element_present(self.ERROR_MESSAGE)

    # ● Test 9
    # - Ia ca o listă toate //label
    # - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
    # - Aici e ok să avem 2 asserturi

    def test_lista_label(self):
        print(f'A inceput testul {self._testMethodName}')
        lista_label_text = self.driver.find_elements(By.XPATH, '//label')
        expected_text_user = 'Username'
        actual_text_user = lista_label_text[0].text
        expected_text_pass = 'Password'
        actual_text_pass = lista_label_text[1].text
        self.assertEqual(expected_text_user, actual_text_user), f"Text doesn't match"
        self.assertEqual(expected_text_pass, actual_text_pass), f"Text doesn't match"

    # ● Test 10
    # - Completează cu user și pass valide
    # - Click login
    # - Verifică ca noul url CONTINE /secure
    # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    # - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def date_valide(self):
        print(f'A inceput testul {self._testMethodName}')
        user = self.driver.find_element(*self.USERNAME)
        user.send_keys("tomsmith")
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("SuperSecretPassword!")
        self.logare()

    def test_secure_area(self):
        print(f'A inceput testul {self._testMethodName}')
        self.date_valide()
        actual_URL = self.driver.current_url
        self.assertIn("/secure", actual_URL), "Noul URL nu contine '/secure'"
        element_flash_success = self.wait(self.SECURE_AREA, 5)
        assert element_flash_success.is_displayed(), 'Element neafisat'
        mesaj = self.driver.find_element(*self.SECURE_AREA).text
        self.assertIn('secure area', mesaj), f"Mesajul {mesaj} nu contine textul 'secure area!'"

    # Test 11
    # - Completează cu user și pass valide
    # - Click login
    # - Click logout
    # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_logout(self):
        print(f"A inceput testul {self._testMethodName}")
        self.date_valide()
        logout_button = self.driver.find_element(By.CLASS_NAME, "icon-signout")
        logout_button.click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Nu ai ajuns pe {expected_url}, esti pe {actual_url}"
