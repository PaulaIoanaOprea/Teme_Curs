"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()

"""


# CLASA
class Cerc:
    # ATRIBUTE
    raza = None
    culoarea = None

    # CONSTRUCTOR

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # METODA
    def descriere_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza de {self.raza} cm')

    # METODA
    def aria_cercului(self, pi, raza):
        pi = 3.14
        aria = pi * self.raza ** 2
        return aria

    # METODA
    def diametru_cerc(self):
        diametru = 2 * self.raza
        return diametru

    # METODA
    def circumferinta_cerc(self):
        pi = 3.14
        circumferinta = 2 * pi * self.raza
        return circumferinta


# OBIECTE

bulgare = Cerc(9, 'roz')
minge = Cerc(12, 'multicolora')

# APELARE METODE PT. OBIECTUL BULGARE

bulgare.descriere_cerc()
print(f'Aria cercului este {bulgare.aria_cercului(3.14, 10)}')
print(f'Diametrul cercului este {bulgare.diametru_cerc()}')
print(f'Circumferinta cercului este {bulgare.circumferinta_cerc()}')

print('')

# APELARE METODE PT. OBIECTUL MINGE

minge.descriere_cerc()
print(f'Aria cercului este {minge.aria_cercului(3.14, 100)}')
print(f'Diametrul cercului este {minge.diametru_cerc()}')
print(f'Circumferinta cercului este {minge.circumferinta_cerc()}')

"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().

"""


# CLASA
class Dreptunghi:
    # ATRIBUTE
    Lungime = 20
    latime = 10
    culoare = 'lila'

    # CONSTRUCTOR

    def __init__(self, Lungime, latime, culoare):
        self.Lungime = Lungime
        self.latime = latime
        self.culoare = culoare

    # METODA
    def descriere_dreptunghi(self):
        print(
            f'Dreptunghi cu lungimea de {self.Lungime} cm., latimea de {self.latime} cm., si de culoare {self.culoare}')

    # METODA
    def aria_dreptunghiului(self):
        aria = self.Lungime * self.latime
        return aria

    # METODA
    def petimetru_dreptunghi(self):
        perimetru = 2 * (self.Lungime + self.latime)
        return perimetru

    # METODA
    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare

    # OBIECTE


tv_plasma = Dreptunghi(20, 10, 'lila')

# APELAM METODE PE OBIECT

tv_plasma.descriere_dreptunghi()
print(f'Aria pt dreptunghi este de {tv_plasma.aria_dreptunghiului()} cm')
print(f'Perimetrul pt dreptunghi este de {tv_plasma.petimetru_dreptunghi()} cm')
tv_plasma.schimba_culoare('multicolor')
tv_plasma.descriere_dreptunghi()

"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)

"""


# CLASA
class Angajat:
    # ATRIBUTE

    nume = None
    prenume = None
    salariu = None

    # CONSTRUCTOR

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    # METODA

    def descriere_angajat(self):
        print(f'Angajatul pe nume {self.nume} {self.prenume}, castiga lunar {self.salariu} lei net')

    # METODA

    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}')

    # METODA

    def salariu_lunar(self):
        print(f'Salariul lunar al angajatului este {self.salariu} lei net')

    # METODA

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariul anual al angajatului este de {salariu_anual} lei net')

    # METODA

    def marire_salariu(self, marire_salariu):
        self.salariu *= (1 + marire_salariu / 100)
        print(f'Salariul angajatului s-a marit cu {marire_salariu} %')


# OBIECT

lucrator = Angajat('Oprea', 'Paula Ioana', 2000)

# APELAM METODE PE OBIECT

lucrator.descriere_angajat()
lucrator.nume_complet()
lucrator.salariu_lunar()
lucrator.salariu_anual()
lucrator.marire_salariu(200)
lucrator.salariu_lunar()

"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)

"""


# CLASA
class Cont:
    # ATRIBUTE
    iban = None
    titular_cont = None
    sold = None

    # CONSTRUCTOR
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    # METODA
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')

    # METODA
    def debitare_cont(self, suma_solicitata):
        if suma_solicitata > self.sold:
            print('Fonduri insuficiente')
        else:
            self.sold = self.sold - suma_solicitata
            print(f'Ati retras suma de {suma_solicitata} lei')

    # METODA
    def creditare_cont(self, imprumut):
        self.sold = self.sold + imprumut
        print(f'Ati creditat suma de {imprumut} lei, adaugata in contul {self.iban}')


# OBIECT

titular = Cont('RO89 RNCB CRT0 2564 1230', 'Oprea Paula Ioana', 6000)

# APLICAM METODELE PE OBIECT
titular.afisare_sold()
titular.debitare_cont(3500)
titular.creditare_cont(12000)
titular.afisare_sold()
