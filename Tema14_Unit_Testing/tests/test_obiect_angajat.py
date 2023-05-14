import unittest

from Teme_Curs.Tema14_Unit_Testing.app.obiect_angajat import Angajat


class TestAngajat(unittest.TestCase):

    def setUp(self):
        self.angajat = Angajat('Oprea', 'Paula Ioana', 4000)

    def tearDown(self):
        pass

    def test_descriere(self):
        self.angajat.descriere_angajat()
        self.assertEquals(self.angajat.nume == 'Oprea', self.angajat.prenume == 'Paula Ioana')

    def test_nume(self):
        self.angajat.nume_complet()
        self.assertTrue(self.angajat.nume_complet() == 'Oprea Paula Ioana')

    def test_salariu_lunar(self):
        self.angajat.salariu_lunar()
        self.assertTrue(self.angajat.salariu_lunar() == 4000)

    def test_salaiu_anual(self):
        self.angajat.salariu_anual()
        self.assertTrue(self.angajat.salariu_anual() == 48000)

    def test_salariu_marit(self):
        self.angajat.marire_salariu(20)
        self.assertTrue(self.angajat.salariu == 4800)

