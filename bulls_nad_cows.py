# bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
# author: Daniel Lehotský
# email: dlehotsk@gmail.com
# discord: daniel_lehotsky
# -----------------------------------------------------------------

import random

def generuj_cislo() -> list[str]:
    """Generuje 4 miestne nahodne cislo s unikatnymi cislicami, 
    nezacina 0 a neobsahuje neciselne znaky.

    Vracia:
        List stringov cislic vygenerovaneho cisla.
    """
    while True:
        cislo = random.randint(1000, 9999)
        if cislo % 10 != 0:
            cislice = set(str(cislo))
            if len(cislice) == 4:
                return list(str(cislo))

def zadaj_cislo() -> str:
    """Uzivatelov input cisla.

    Vracia:
        String cislic zo zadaneho cisla.
    """

    while True:
        zadane_cislo = input("Hadaj cislo: ")
        if not vyhodnot_cislo(zadane_cislo):
            continue
        return zadane_cislo
    
def vyhodnot_cislo(cislo: str) -> bool:
    """Vyhodnocuje cislo, ktore by nemalo zacinat 0, 
    nemalo by mat iny pocet cislic ako 4, nemalo by obsahovat neciselne znaky
    a cislice musia byt unikatne. 

    Args:
            cislo: Vyhodnocovane zadane cislo.

    Vracia:
            True ak cislo zodpoveda zadanym podmienkam, inak False. 
    """

    if len(cislo) != 4:
        print("Prosim zadaj iba 4 miestne cislo.")
        return False
    if cislo[0] == '0':
        print("Cislo nesmie zacinat 0.")
        return False
    for char in cislo:
        if not char.isdigit():
            print("Cislo nesmie obsahovat neciselne znaky.")
            return False
    cislicaset = set()
    for cislica in cislo:
        if cislica in cislicaset:
            print("Cislice sa nesmu opakovat.")
            return False
        cislicaset.add(cislica)
    return True

def vyhodnotenie(vyhodnot_cislo: str, zadane_cislo: str) -> list[int]:
    """Pocita pocet bulls a cows v zadanom cisle.

    Args:
        vyhodnot_cislo: Vygenerovane nezname 4-miestne cislo.
        zadane_cislo: Cislo, ktore zadal uzivatel.

    Vracia:
        List dvoch integerov, kde prve cislo je pocet bulls a druhe pocet cows.
    """

    bulls = 0
    cows = 0
    for i, cislo in enumerate(zadane_cislo):
        if cislo == vyhodnot_cislo[i]:
            bulls += 1
        elif cislo in vyhodnot_cislo:
            cows += 1
    return [bulls, cows]

def mn_cislo(slovo: str, pocet: int) -> str:
    """Vypise slovo v mnoznom cisle.

    Args:
        slovo: Hodnotene slovo.
        pocet: Pocet, kolko krat sa slovo vyskytuje.

    Vracia:
        Slovo, ktore ked ma pocet viac ako 1, ma pismeno "s" na konci.
    """

    if pocet == 1:
        return slovo
    else:
        return slovo + "s"
    
def bulls_and_cows() -> None:
    """Priebeh hry Bulls and Cows"""

    print('----------------------------')
    print('Vitaj v hre Bulls and Cows.')
    print('Vygeneroval som pre teba 4 miestne cislo.')
    print('-----------------------------------------')

    tajne_cislo = generuj_cislo()
    pokusy = 0    

    while True:
        uziv_cislo = zadaj_cislo()
        bulls, cows = vyhodnotenie(tajne_cislo, uziv_cislo)
        print("{} {} and {} {}.".format(bulls, mn_cislo("bull", bulls), cows, mn_cislo("cow", cows)))
        pokusy += 1
        if bulls == 4:
            print("Gratulujem! Cislo si uhadol na {}. pokus".format(pokusy))
            break    
               
if __name__ == "__main__":
    bulls_and_cows()