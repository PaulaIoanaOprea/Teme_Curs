import unittest

from Teme_Curs.Tema14_Unit_Testing.app.obiect_dreptunghi import Dreptunghi


class TestDreptunghi(unittest.TestCase):

    def setUp(self):
        self.dreptunghi = Dreptunghi(20, 10, 'lila')

    def tearDown(self):
        pass

    def test_descriere(self):
        self.dreptunghi.descriere_dreptunghi()
        self.assertEquals(self.dreptunghi.Lungime == 20, self.dreptunghi.latime == 10,
                          self.dreptunghi.culoare == 'lila')

    def test_arie(self):
        assert self.dreptunghi.aria_dreptunghiului() == 200

    def test_perimetru(self):
        assert self.dreptunghi.perimetru_dreptunghi() == 60

    def test_culoare_noua(self):
        self.dreptunghi.schimba_culoare('alb')
        assert self.dreptunghi.culoare == 'alb'





