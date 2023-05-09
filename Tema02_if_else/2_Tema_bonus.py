# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = int(input('introdu x'))
if len(str(abs(x))) >= 4:
    print('Are minim 4 cifre')
else:
    print('Nu are minim 4 cifre')

# 2. Verifica daca x are exact 6 cifre

x = int(input('introdu x'))
if len(str(x)) >= 6:
    print('Are exact 6 cifre')
else:
    print('Nu are 6 cifre')

# 3. Verifica daca x este numar par sau impar

x = int(input('introdu x'))
if x % 2 == 0:
    print('par')
else:
    print('impar')

# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele

x = int(input('Introdu x'))
y = int(input('Introdu y'))
z = int(input('Introdu z'))
if x >= y and x >= z:
    print(f'{x} este cel mai mare numar')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar')
else:
    print(f'{z} este cel mai mare numar')

'''
5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
lungimea celei de-a treia laturi)
'''

x = int(input('Introdu x'))
y = int(input('Introdu y'))
z = int(input('Introdu z'))
suma_xyz = x + y + z
print(suma_xyz)
if suma_xyz == 180:
    print('triunghiul este valid')
else:
    print('triunghiul nu este valid')

'''
6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
smarte'
'''
string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti x'))
print(string[:-x:])

'''
7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
din primele 5 caractere + ultimele 5
'''

string = 'Coral is either the stupidest animal or the smartest rock'
string_1 = string[0:5] + string[-5:]
print(string_1)

'''8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
animal or the smartest '
'''

string = 'Coral is either the stupidest animal or the smartest rock'
print(string.find('rock'))
print(string[:53])

'''
9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
functie pentru a face string-ul case insensitive)
'''

string = input('Introduceti un cuvant oarecare').casefold()
print(string)
assert string[0:1] == string[-1:0], 'Primul si ultimul caracter nu sunt diferite'
print('Primul si ultimul caracter sunt diferite')

'''
10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
(hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
'''
string = '0123456789'
print(f'numere pare sunt: {string[0::2]}')
print(f'numere impare sunt: {string[1::2]}')
