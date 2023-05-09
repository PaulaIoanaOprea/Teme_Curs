##### Exercitii bonus #####

"""
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""


def numere_comune(lista1, lista2):
    comune = set()
    for i in lista1:  # parcurgem cele doua liste
        for j in lista2:
            if i == j:
                comune.add(i)
    return comune


lista1 = [1, 3, 2, 5, 6, 7, 9, 12, 3]
lista2 = [3, 5, 7, 9, 10, 2, 4, 6, 1]
print(f"Elementele comune din cele doua liste sunt : {numere_comune(lista1, lista2)}")

"""
2. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
"""


def reducere_pret(pret_produs, reducere):
    if reducere in range(0, 100):
        print("Reducere invalida")
    else:
        pret_final = pret_produs - (pret_produs * (reducere / 100))
        return pret_final


pret_produs = float(input("Introduceti pretul produsului : "))
reducere = int(input("Introduceti reducerea in % pentru produs : "))
if reducere in range(0, 100):
    print(f"Pretul final al produsului este de {reducere_pret(pret_produs, reducere)} lei")
else:
    print("Reducere invalida")


"""
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
"""

import datetime
import pytz


def data_ora_curenta(time_zone):
    zona = pytz.timezone(time_zone)
    data_ora = datetime.datetime.now(zona)
    return data_ora


print(f"Data si ora in Romania: {data_ora_curenta(time_zone='Europe/Bucharest')}")
print(f"Data si ora in China:   {data_ora_curenta(time_zone='Asia/Hong_Kong')}")

