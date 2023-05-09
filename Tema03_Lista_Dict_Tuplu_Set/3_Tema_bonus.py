"""
1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
Google search hint: “how to check if item is in list python”

"""

lista_jucatori_teren = ['Hagi', 'Popescu', 'Mutu', 'Petrescu', 'Chivu']
lista_jucatori_rezerva = ['Tanase', 'Tamas', 'Chiriches', 'Raducioiu', 'Marica']
lista_jucatori_scosi = []
schimbari_efectuate = 0
schimbari_max = 3

print(lista_jucatori_teren)
print(lista_jucatori_rezerva)
while schimbari_efectuate < schimbari_max:
    jucator_intrat = input(f'Introdu jucatorul care intra din {lista_jucatori_rezerva}')
    jucator_iesit = input(f'Introdu jucatorul care iese din {lista_jucatori_teren}')
    if jucator_intrat in lista_jucatori_rezerva and jucator_iesit in lista_jucatori_teren:
        lista_jucatori_teren.remove(jucator_iesit)
        lista_jucatori_scosi.append(jucator_iesit)
        lista_jucatori_teren.append(jucator_intrat)
        lista_jucatori_rezerva.append(jucator_intrat)
        schimbari_efectuate += 1
        print(f'Prima schimbare: {jucator_intrat} intra, {jucator_iesit} iese. Mai puteti efectua {schimbari_max-schimbari_efectuate} schimbari.')
    elif jucator_iesit not in lista_jucatori_teren:
        print(f'Nu puteti efectua schimbarea: {jucator_iesit} nu este in teren')
    else:
        print(f'Mai puteti efectua: {schimbari_max-schimbari_efectuate} schimbari')









