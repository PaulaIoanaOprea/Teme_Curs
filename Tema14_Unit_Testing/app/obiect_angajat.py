class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        print(f'Angajatul se numenste {self.nume} {self.prenume}, si castiga lunar {self.salariu} Ron, net')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        salariu_anual = 12 * self.salariu
        return salariu_anual

    def marire_salariu(self, procent_marire_salariu):
        self.salariu *= (1 + procent_marire_salariu / 100)
        # self.salariu = self.salariu + (self.salariu * (procent_marire_salariu / 100))
        return self.salariu

