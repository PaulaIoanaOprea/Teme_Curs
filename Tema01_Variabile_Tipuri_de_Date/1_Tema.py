"""
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

Variabila - un loc din memorie in care punem valori, tinem anumite date
          - o cutie in care  punem diferite obiecte de care avem nevoie
"""

"""
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
"""
telefon_mobil = 'nokia' #string
model_telefon = 'smart'

ani_de_liceu = 4 #integer

nota_tema = 5.75 #float

imi_plac_pisicile = True #bool

"""
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
"""
print(type(telefon_mobil))
print(type(model_telefon))
print(type(ani_de_liceu))
print(type(nota_tema))
print(type(imi_plac_pisicile))

"""
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
"""
nota_tema = round(nota_tema)
print(round(nota_tema))
print(type(nota_tema))

"""
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""
print(f'Am primit un telefon, este marca {telefon_mobil}, de tipul {model_telefon}')
print(f'Am uitat toata informatica din cei {ani_de_liceu} ani de liceu')
print(f'Pentru tema anterioara nu cred ca merit nici macar nota {nota_tema}')
print(f'Locuiesc la curte si imi plac animalele {imi_plac_pisicile}')


"""
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
"""
numele = input('Introdu numele' )
prenumele = input('Introdu prenumele')
nume_complet = (len(numele)+len(prenumele))
print(nume_complet)
print(f'Numele complet are {nume_complet} caractere')

"""
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
"""
lungimea = int(input('Va rugam introduceti lungimea'))
latimea = int(input('Va rugam introduceti latimea'))
print(f'Aria dreptunghiului este {lungimea*latimea}')

"""
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
"""
text = 'Coral is either the stupidest animal or the smartest rock'
cuvant_the = text.split()
print(cuvant_the.count('the'))

"""
9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
"""

text = 'Coral is either the stupidest animal or the smartest rock'
print(text.replace('the','THE'))

"""
10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
"""
text_1 = 'Coral is either the stupidest animal or the smartest rock'
text_2 = text_1.isdigit()
print(type(text_2))
assert text_2 == False, 'Eroare! Acest string nu contine numere.'
print('Am verificat assert-ul, textul are doar litere!')











