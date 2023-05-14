class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban_eu, nume_complet, sold_eu):
        self.iban = iban_eu
        self.titular_cont = nume_complet
        self.sold = sold_eu

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma_solicitata):
        sold_ramas = self.sold - suma_solicitata
        return sold_ramas

    def creditare_cont(self, imprumut):
        sold_disponibil = self.sold + imprumut
        return sold_disponibil
