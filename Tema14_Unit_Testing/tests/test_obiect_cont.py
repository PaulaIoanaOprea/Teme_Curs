import unittest

from Teme_Curs.Tema14_Unit_Testing.app.obiect_cont import Cont


class TestCont(unittest.TestCase):

    def setUp(self):
        self.cont = Cont('EU458964123', 'Oprea Paula Ioana', 6000)

    def tearDown(self):
        pass

    def test_afisare_sold(self):
        self.cont.afisare_sold()
        self.assertEquals(self.cont.iban == 'EU458964123', self.cont.titular_cont == 'Oprea Paula Ioana',
                          self.cont.sold == 6000)

    def test_debitare_sold(self):
        self.cont.debitare_cont(1500)
        assert self.cont.sold == 4500

    def test_creditare_cont(self):
        self.cont.creditare_cont(2000)
        self.assertTrue(self.cont.sold == 8000)
