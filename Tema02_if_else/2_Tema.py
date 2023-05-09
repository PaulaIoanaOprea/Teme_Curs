""" Pentru toate exercitiile se va folosi notiunea de if in rezolvare. Indirect veti exersa si operatorii in
cadrul conditiilor ramurilor din if
Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod sau citita de la
tastatura, dupa preferinte si va fi o variabila int

1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

If Else  - evalueaza conditii si bifurca codul in fuctie de rezultat; In cazul in care conditia if = True, nu mai
intervine else

"""

'''2.Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai
mare ca 0)
'''
nr_natural = int(input('Introdu valoarea lui x'))
if nr_natural > 0:
    print('x este numar natural')
else:
    print('x nu este numar natural')

# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

nr_x = int(input('Introdu valoarea lui x'))
if nr_x > 0:
    print('x este numar pozitiv')
elif nr_x < 0:
    print('x este numar negativ')
else:
    print('x este numar neutru ')

# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x_interval = int(input('x este egal cu:'))
if (x_interval >= -2 and x_interval <= 13):
    print('x apartine intervalului [-2,13]')
else:
    print('x nu apartine intervalului [-2,13]')

'''5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs
'''
nr_x = 15
nr_y = 9
diferenta_numere = abs(nr_x - nr_y)
print(diferenta_numere)
if diferenta_numere < 5:
    print('A mers')
else:
    print('mai incearca, schimba numerele')

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

x = int(input('x = '))
y = int(input('y = '))
if not (5 <= x <= 27):
    print(f'Nr {x}, nu se afla in intervalul [5:27]')
else:
    print(f'Nr {x}, se afla in intervalul [5:27]')

'''7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
daca nu, afiseaza care din ele este mai mare
'''
nr_x = 9
nr_y = 15
if nr_x == nr_y:  # False
    print('x este egal cu y')
elif nr_x < nr_y:
    print('x este mai mic decat y')
else:
    print('y este mai mare decat x')

'''8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala)
'''
nr_x = 8
nr_y = 6
nr_z = 2
if nr_x == nr_y == nr_z:
    print('triunghiul este echilateral')
elif (nr_x == nr_y) or (nr_x == nr_z) or (nr_y == nr_z):
    print('triunghiul este isoscel')
else:
    print('triunghiul este oarecare')

'''9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
'''
litera = input('Introduceti litera')
if litera.lower() in 'aeiou' and litera.isalpha():
    print('Aceasta litera este o vocala')
elif not litera.isalpha():
    print('Aceasta nu este o litera')
else:
    print('Aceasta este o consoana')

'''
10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F
'''
nota = int(input('Introduceti nota'))
if nota > 9:
    print('Ai luat A')
elif nota > 8:
    print('Ai luat B')
elif nota > 7:
    print('Ai luat C')
elif nota > 6:
    print('Ai luat D')
elif nota > 5:
    print('Ai luat E')
elif nota > 4:
    print('Ai luat F')
else:
    print('Ai picat')
