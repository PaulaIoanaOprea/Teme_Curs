# 1.Funcție care să calculeze și să returneze suma a două numere

def calculeaza_suma_a_doua_numere():
    x = int(input('x ='))
    y = int(input('y ='))
    suma = x + y
    return suma


print(f'Suma dintre numerele x si y este egala cu: {calculeaza_suma_a_doua_numere()} ')

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

i = int(input('Introdu numarul'))


def valoare_True_sau_False(i):
    return i % 2 == 0


print(valoare_True_sau_False(i))

"""3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""


def total_caractere_nume_complet():
    nume_prenume = input(f'Introduceti numele dumneavoastra complet')
    nume_prenume = len(nume_prenume)
    print(f'Numele dumneavoastra contine {nume_prenume} caractere')


total_caractere_nume_complet()


# 4. Funcție care returnează aria dreptunghiului

def aria_dreptunghiului():
    L = int(input('Introduceti lungimea dreptunghiului'))
    l = int(input('Introduceti latimea dreptunghiului'))
    aria = L * l
    return aria


print(f'Aria dreptunghiului este: {aria_dreptunghiului()}')


# 5. Funcție care returnează aria cercului

def aria_cercului():
    pi = 3.14
    r = int(input('Raza ='))
    aria = pi * r ** 2
    return aria


print(f'Aria cercului este {aria_cercului()}')

"""6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.
"""


def true_false(string):
    if 'x' in string:
        return True
    else:
        return False


print(true_false('Gaseste un caracter x'))
print(true_false('Gaseste un caracter'))

"""7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""


def up_low(string):
    upper_y = 0
    lower_x = 0
    for i in string:
        if i.isupper():
            upper_y += 1
        else:
            lower_x += 1
    print(f'upper case {upper_y}')
    print(f'lower case {lower_x}')


up_low('OpReA paula IOANA')

"""8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""

lista = [9, 21, 17, -9, -21, -17, 0, 11, -3, 15]


def numere_pozitive(lista):
    lista_pozitive = []
    for numar in lista:
        if numar > 0:
            lista_pozitive.append(numar)
    return lista_pozitive


lista_pozitive = numere_pozitive(lista)

print(lista_pozitive)

"""9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""

x = int(input(f'Introduceti un numar'))
y = int(input(f'Introduceti alt numar'))


def comparare():
    if x > y:
        print(f' Primul numar {x} este mai mare decat al doilea numar {y}')
    elif y > x:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print(f'Numerele sunt egale')


comparare()

"""10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""

nr = int(input(f'Introdu un numar'))
set = {-3, 5, 0, 4, 9, -7}


def adaugare_nr_set(nr, set):
    if nr in set:
        print(f"Nu am adaugat numarul {nr} in set.")
        return False
    else:
        set.add(nr)
        print(f"Am adaugat numarul nou in set.Acesta este numarul {nr}")
        return True


concluzie = adaugare_nr_set(nr, set)

if concluzie:
    print(f"Numarul {nr} a fost adaugat cu succes in set")
else:
    print(f"Numarul {nr} exista deja in set.")
