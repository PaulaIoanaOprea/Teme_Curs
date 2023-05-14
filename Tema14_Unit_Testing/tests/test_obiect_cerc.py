import unittest

from Teme_Curs.Tema14_Unit_Testing.app.obiect_cerc import Cerc


class TestCerc(unittest.TestCase):

    def setUp(self):
        self.cerc = Cerc(10, 'nonculoare')

    def tearDown(self):
        pass

    def test_descriere(self):
        self.cerc.descriere_cerc()
        self.assertEquals(self.cerc.raza == 10, self.cerc.culoare == 'nonculoare')

    def test_arie(self):
        self.cerc.aria_cercului()
        self.assertTrue(self.cerc.aria_cercului() == 314)

    def test_diametru(self):
        self.cerc.diametru_cerc()
        self.assertTrue(self.cerc.diametru_cerc() == 20)

    def test_circumferinta(self):
        self.cerc.circumferinta_cerc()
        assert self.cerc.circumferinta_cerc() != 62.80

