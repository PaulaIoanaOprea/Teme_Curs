"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

"""
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14
    culoare = 'Mov'

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):  # mostenire
    __latura = 5  # incapsulare

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    def get_latura(self):
        return self.__latura

    def delete_latura(self):
        del self.__latura

    def set_latura(self, latura):
        if latura == self.__latura:
            print('Toate laturile sunt egale')
        else:
            print('Forma geometrica nu este patrat')


noptiera = Patrat(10)

noptiera.descriere()
print(f'Latura noptierei este: {noptiera.get_latura()}')
noptiera.set_latura(10)
noptiera.set_latura(10)
noptiera.delete_latura()

latura_noptiera = noptiera.get_latura()

print(f"Latura noptierei este: {latura_noptiera}")

print(f'Aria noptierei este egala cu {noptiera.aria()}')


class Cerc(FormaGeometrica):
    __raza = None
    culoare = "incolor"

    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        if raza <= 0:
            print("Raza este prea mica")
        else:
            self.__raza = raza

    def delete_raza(self):
        del self.__raza

    def aria(self):
        return self.PI * self.__raza * self.__raza

    def descriere(self):
        super().descriere()

        print("Eu nu am colturi, sunt rotund")

        print(f"Initial am fost {super().culoare} iar acum sunt {self.culoare}")


balon = Cerc(3)
balon.descriere()
print(f"Aria cercului este {balon.aria()}")
balon.delete_raza()
balon.set_raza(10)
balon.get_raza()

