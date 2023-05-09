##### Exercitii optionale #####

"""
1. Funcție care primește o lună din an și returnează câte zile are acea luna
"""


def luna_an(luna):
    zile_luna = {
        "ianuarie": 31,
        "februarie": 28,
        "martie": 31,
        "aprilie": 30,
        "mai": 31,
        "iunie": 30,
        "iulie": 31,
        "august": 31,
        "septembrie": 30,
        "octombrie": 31,
        "noiembrie": 30,
        "decembrie": 31,
    }
    if luna.lower() in zile_luna:
        print(f"Luna '{luna.lower()}' are {zile_luna[luna.lower()]} zile calendaristice.")
    else:
        print(f"Luna '{luna}' nu exista. Introdu o luna valida")


luna = input("Introduceti o luna din an : ")
luna_an(luna)

"""
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
"""


def calculator(nr1, nr2):
    # suma, diferenta, inmultirea, impartirea = 0, 0, 0, 0
    a = nr1 + nr2
    b = nr1 - nr2
    c = nr1 * nr2
    d = nr1 / nr2
    return a, b, c, d


nr1 = int(input("a = "))
nr2 = int(input("b = "))
a, b, c, d = calculator(nr1, nr2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

"""
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""


def return_dict(lista):
    nr_ori = {}  # declaram un dict gol
    for nr in lista:  # parcurgem lista
        nr_ori[nr] = lista.count(
            nr)  # adaugam in dict-ul 'nr_ori': cheia 'nr' cu valoarea 'de cate ori apare in lista acel nr'
    return nr_ori


lista = [1, 4, 5, 3, 5, 4, 6, 8, 9, 8]
print(f"Cifrele din lista introdusa apar dupa cum urmeaza: {return_dict(lista)}")

"""
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
"""


def trei_numere(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(f"Cel mai mare numar este: {trei_numere(a, b, c)}")

"""
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
"""


def suma_pana_la_nr(x):
    suma = 0
    for i in range(0, x + 1):  # mergem pana la x+1 ca nu ia si capatul de interval
        suma += i
        if i < x:  # am pus acest if doar ca sa afiseze 'frumos' in consola :)
            print(i, "+ ", end="")
        else:
            print(i, "= ", end="")
    return suma


print(suma_pana_la_nr(6))
