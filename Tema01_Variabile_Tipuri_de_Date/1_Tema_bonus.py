"""
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
"""
cuvant_impar = (input('Va rugam intruduceti cuvantul:'))
if len(cuvant_impar) % 2 != 0:
   litera_mijloc = cuvant_impar [len(cuvant_impar) // 2]
   print(f'Caracterul din mijloc este {litera_mijloc}')
else:
   print(f'Cuvantul introdus nu este impar')

"""
2. Folosind assert, verifică dacă un string este palindrom.
"""
palindrom = input('Introduceti un cuvant palindrom:')
Paula = palindrom[::-1]
assert palindrom == Paula , f'Cuvantul {palindrom} nu este un palindrom'
print (f' Cuvantul {palindrom} este un palindrom')

"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""
text, text_1 = input('Introduceti variabilele de la tastatura:').split()
print(text)
print(text_1)

"""
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""
string = input('Introdu string:')
string_1 = string [0]
string_final = string_1+string[1:-1].replace(string_1, string_1.upper())+string[-1]
print(string_final)

"""
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
"""
user = input('Introduceti user-ul:')
parola = input('Introduceti parola:')
print(f"Parola pt user {user} este {'*' * len(parola)} si are {len(parola)} caractere")











