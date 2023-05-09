"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""

lista_masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in range(len(lista_masini)):
    print(f'Masina mea preferata este :{lista_masini[i]}')


for masina in lista_masini:
    print(f'Masina mea preferata este: {masina}')

i = 0
while i < len(lista_masini):
    print(f'Masina mea preferata este: {lista_masini[i]}')
    i += 1

"""
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
"""

lista_masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in range(1, (len(lista_masini) -1)):
    lista_masini[i] = lista_masini[i].upper()
else:
    print(f'Lista modificata cu majuscule este: {lista_masini}')

"""
 3.Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘

"""
lista_masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for masina in lista_masini:
    if masina == 'Mercedes':
        print(f'Am gasit masina dorita de dvs: {masina}')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

"""
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""
lista_masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for masina in lista_masini:
    if masina == 'Lăstun' or masina == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

"""
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
"""
lista_masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
masini_vechi = []
for rabla in lista_masini:
    if rabla == 'Lăstun':
        masini_vechi.append(rabla)
        lista_masini.insert(lista_masini.index('Lăstun'), 'Tesla')
        lista_masini.pop(lista_masini.index('Lăstun'))
    if rabla == 'Trabant':
        masini_vechi.append(rabla)
        lista_masini.insert(lista_masini.index('Trabant'), 'Tesla')
        lista_masini.pop(lista_masini.index('Trabant'))
print(f'Modele noi :{lista_masini}')
print(f'Modele vechi: {masini_vechi}')

"""
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
"""

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

buget = 15000
print(pret_masini.items())
for masina, pret in  pret_masini.items():
    if pret <= buget:
        print(f'Acestea sunt masinile pentru bugetul dvs: {masina}')
for masina in pret_masini.keys():
    if pret_masini[masina] <= buget:
        print(f'Pentru un buget de sub {buget}, puteti alege masina: {masina}')

"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
trei = 0
for trei in numere:
    if trei == 3:
        trei += 1
print(f'Cifra trei apare de {trei} ori')

"""
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s = 0
for suma in numere:
    s += suma
print(f'Suma nr din lista este: {s}')

"""
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_max = 0
for i in range (len(numere)):
    if numere[i] > nr_max:
        nr_max = numere[i]
print(f'Cel mai mare nr din lista este:{nr_max}')

"""
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = - numere[i]
print(numere)

