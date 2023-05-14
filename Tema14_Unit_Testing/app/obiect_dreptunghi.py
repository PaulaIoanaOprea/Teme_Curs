"""
La tema 6 ati avut de facut clase.
1. Obligatoriu UNIT TESTS pt ex2 - clasa Dreptunghi
● Clasa Dreptunghi
● Atribute: lungime, latime, culoare
● Constructor pt toate atributele
● Metode:
● descrie()
● aria()
● perimetrul()
● schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si param o noua culoare si va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
1. Unit tests pt toate metodele
● Cum poti testa totusi schimba culoarea daca nu returneaza nimic?
● Fie verificati direct valoarea atributului, fie verif ce returneaza metoda
descrie()
"""


class Dreptunghi:
    Lungime = None
    latime = None
    culoare = None

    def __init__(self, latura_mare, latura_mica, culoare_lila):
        self.Lungime = latura_mare
        self.latime = latura_mica
        self.culoare = culoare_lila

    def descriere_dreptunghi(self):
        print(f'Dreptunghiul are lungimea de {self.Lungime} cm., latimea de {self.latime} cm., si este de culoare'
              f' {self.culoare}')

    def aria_dreptunghiului(self):
        aria = self.Lungime * self.latime
        return aria

    def perimetru_dreptunghi(self):
        perimetru = 2 * (self.Lungime + self.latime)
        return perimetru

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare





