# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Daniel Lehotský
# email: dlehotsk@gmail.com
# discord: Daniel Lehotský#8147
# -------------------------------------------------------------

from pprint import pprint

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# +------+-------------+
# | user |   password  |
# +------+-------------+
# | bob  |     123     |
# | ann  |   pass123   |
# | mike | password123 |
# | liz  |   pass123   |
# +------+-------------+

oddelovac = 52 * "-" 
uzivatelia = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}

# zadanie mena a hesla
meno = input('Zadaj tvoje meno:')
heslo = input('Zadaj tvoje heslo:')

# privitanie uzivatelia a zadanie cisla analyzovaneho textu
if uzivatelia.get(meno) == heslo:
    print(oddelovac)
    print(f'Ahoj {meno}, vitaj v aplikácii textový analyzátor.\nNa výber sú tri texty.')
    print(oddelovac)
    print("Vyber číslo textu od 1 do 3, ktorý chceš analyzovať:")
    cislo = input()

    print(oddelovac)

# overenie zadaneho znaku cez vnorenu podmienku a cyklus FOR pre celkovy pocet slov
    rozdeleny_text = []
    
    if cislo.isnumeric():
        if int(cislo) >= 1 and int(cislo) <= 3:
            for slovo in TEXTS[int(cislo) - 1].split():
                ciste_slovo = slovo.strip('.,')
                rozdeleny_text.append(ciste_slovo)
        else:
            print("Zadané číslo nie je od 1 do 3. Ukončujem program.")
            quit()
    else:
        print("Boli zadané nepovolené znaky. Ukončujem program.")
        quit()

    celkovy_pocet = len(rozdeleny_text)
    print("Celkový počet slov v texte:", celkovy_pocet)

# POZNÁMKA: Nevedel som ako postupovať aby pri zadaní napr. záporného, 
# alebo desatinného čísla vypísal tú istú hlášku, ktorú píše pri zadaní kladného 
# čísla väčšieho ako tri (riadok 72). Ale prišlo mi, že hláška, 
# že bol zadaný nepovolený znak (riadok 75) by mohla stačiť.
# Ak to takto nestačí, tak sa to posnažím prepracovať.

# pocet slov zacinajucich velkym pismenom
    zaciatocne_velke = []

    for slovo in rozdeleny_text:
        if slovo.istitle():
            zaciatocne_velke.append(slovo)

    pocet_zac_velke = len(zaciatocne_velke)
    print("Počet slov začínajúcich veľkým písmenom:", pocet_zac_velke)

# pocet slov velkym pismom
    vsetko_velke = []

    for slovo in rozdeleny_text:
        if slovo.isupper() and slovo.isalpha():
            vsetko_velke.append(slovo)

    pocet_vsetko_velke = len(vsetko_velke)
    print("Počet slov so všetkými písmenani veľkými:", pocet_vsetko_velke)

# pocet slov malym pismom
    malym_pismom = []

    for slovo in rozdeleny_text:
        if slovo.islower():
            malym_pismom.append(slovo)

    pocet_male = len(malym_pismom)
    print("Počet slov malým písmom:", pocet_male)

# pocet cisel v texte
    cisla = []

    for slovo in rozdeleny_text:
        if slovo.isnumeric():
            cisla.append(slovo)
        
    pocet_cisel = len(cisla)
    print("Počet čísel v texte:", pocet_cisel)

# suma vsetkych cisel v texte 
    suma_cisel = sum([int(x) for x in cisla])
    print("Suma čísel v texte:", suma_cisel)

# ak uzivatel zada zle meno alebo heslo            
else:
    print("Uživateľské meno alebo heslo sú nesprávne. Ukončujem program.")
    quit()

# spocitanie poctu pismen v slovach
dlzky_slov = []

for slovo in rozdeleny_text:
    dlzka_jedneho_slova = len(slovo)
    dlzky_slov.append(dlzka_jedneho_slova)

# zoradenie slov podla dlzky
zoradene_dlzky = sorted(dlzky_slov)
dlzky_pocet = {}

for hodnota in zoradene_dlzky:
    if hodnota not in dlzky_pocet:
        dlzky_pocet[hodnota] = 1
    else:
        dlzky_pocet[hodnota] += 1

# vypis jednoducheho stlpcoveho grafu
print(oddelovac)
print("DĹŽKA |      VÝSKYT      | POČET")
print(oddelovac)

for key, value in sorted(dlzky_pocet.items()):
    print(f"{key:>6}|{value*'*':<18}|{value}")

print(oddelovac) 

# POZNÁMKA: Pri tvorení stĺpcového grafu som sa snažil nejak dosiahnuť 
# aby šírka stredného stĺca s hviedičkami určujúcimi výskyt, platila univerzálne 
# pre akýkoľvek zadaný text, ale zadal som tam len formátovanie šírku 18 znakov,
# keďže v našich textoch je najväčší výskyt 17 krát. Ak by presiahol 18, už by
# to trčalo do "stĺpca" POČET. Ale tiež som zatiaľ neprišiel na to ako to urobiť. 
# Na nete som našiel rôzne pokročilé tipy, ale to som nechcel zbytočne hádzať do kódu, 
# keď sme sa podobné postupy ešte neučili. Tak snáď je to takto OK.