"""
1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte
Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
"""


def verificare_imbarcare(varsta, pasaport, insotit_tata, insotit_mama, act_permisiune_mama, act_permisiune_tata):
    if varsta >= 18 and pasaport:
        return True

    elif varsta < 18 and pasaport and insotit_tata and insotit_mama:
        return True

    elif varsta < 18 and pasaport and (
            (insotit_mama and act_permisiune_tata) or (insotit_tata and act_permisiune_mama)):
        return True

    else:
        return False


# are peste 18 ani, Nu are pasaport, fara mama, fara tata, fara permisiune mama, fara permisiune tata == Nu poate calatori
assert verificare_imbarcare(19, False, False, False, False, False) == False

# are sub 18 ani, are pasaport, cu mama, cu tata, fara permisiune mama, fara permisiune tata == Poate calatori
assert verificare_imbarcare(17, True, True, True, False, False) == True

# are sub 18 ani, are pasaport, cu tata, fara mama, permisiune de la mama, fara permisiune de la tata == Poate calatori
assert verificare_imbarcare(15, True, True, False, True, False) == True

# are sub 18 ani, are pasaport, fara tata, cu mama, fara permisiune de la mama, cu permisiune de la tata == Poate calatori
assert verificare_imbarcare(14, True, True, True, False, True) == True

# are sub 18 ani, nu are pasaport, fara tata, cu mama, fara permisiune mama, fara permisiune tata == Nu poate calatori
assert verificare_imbarcare(16, False, False, True, False, False) == False
