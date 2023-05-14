class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Cercul este de culoare {self.culoare}, si are raza de {self.raza} cm')

    def aria_cercului(self):
        pi = 3.14
        aria = pi * self.raza ** 2
        return aria

    def diametru_cerc(self):
        diametru = 2 * self.raza
        return diametru

    def circumferinta_cerc(self):
        pi = 3.14
        circumferinta = 2 * pi * self.raza
        return circumferinta

