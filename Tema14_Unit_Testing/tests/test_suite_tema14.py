import unittest

import HtmlTestRunner

from Teme_Curs.Tema14_Unit_Testing.tests.test_obiect_cerc import TestCerc
from Teme_Curs.Tema14_Unit_Testing.tests.test_obiect_cont import TestCont
from Teme_Curs.Tema14_Unit_Testing.tests.test_obiect_angajat import TestAngajat
from Teme_Curs.Tema14_Unit_Testing.tests.test_obiect_dreptunghi import TestDreptunghi


class TestSuite(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCerc),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCont),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAngajat),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDreptunghi),

        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Raport Test Suite Tema 14",
            report_name="Test Results Tema 14"
        )

        runner.run(teste_de_rulat)
