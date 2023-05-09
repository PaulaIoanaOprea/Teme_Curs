"""
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul
"""
import unittest

import HtmlTestRunner

from Tema10_Suite_de_Teste.tests.test_01_alerts import TestAlerts
from Tema10_Suite_de_Teste.tests.test_02_authentication import TestFirefoxAuthentication
from Tema10_Suite_de_Teste.tests.test_03_context_menu import TestContextMenu
from Tema10_Suite_de_Teste.tests.test_04_keys import TestKeys
from Tema10_Suite_de_Teste.tests.test_05_dropdown import TestDropdown
from Tema09_Tipuri_cu_verificari.Tema_9 import Login


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFirefoxAuthentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDropdown),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="My first test report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)

