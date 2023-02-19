from pojistenci import Pojistenci
from pojisteny import Pojisteny

pojistenci = Pojistenci()


while True:
    print("Pro správu pojištěných pokračujte výběrem z akcí níže. Pro vyvolání akce zadejte číslo akce.")
    print("1. Přidej pojištěného")
    print("2. Hledej pojištěného podle jména")
    print("3. Hledej pojištěného podle příjmení")
    print("4. Hledej pojištěného podle věku")
    print("5. Hledej pojištěného podle telefonního čísla")
    print("6. Hledej pojištěného podle jména a příjmení")
    print("7. Zobraz všechny pojištěné")
    volba = input("Pro výběr akce zadejte číslo akce: ")

    if volba == "1":
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = input("Zadejte věk: ")
        telefon = input("Zadejte telefonní číslo: ")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        pojistenci.pridej_pojisteny(pojisteny)

    elif volba == "2":
        jmeno = input("Zadejte jméno: ")
        vysledek = pojistenci.hledej_podle_jmena(jmeno)
        if vysledek:
            for pojisteny in vysledek:
                print(pojisteny)
        else:
            print("Nenalezen žádný záznam.")

    elif volba == "3":
        prijmeni = input("Zadejte příjmení: ")
        vysledek = pojistenci.hledej_podle_prijmeni(prijmeni)
        if vysledek:
            for pojisteny in vysledek:
                print(pojisteny)
        else:
            print("Nenalezen žádný záznam.")

    elif volba == "4":
        vek = input("Zadejte věk: ")
        vysledek = pojistenci.hledej_podle_vek(vek)
        if vysledek:
            for pojisteny in vysledek:
                print(pojisteny)
        else:
            print("Nenalezen žádný záznam.")

    elif volba == "5":
        telefon = input("Zadejte telefonní číslo: ")
        vysledek = pojistenci.hledej_podle_telefonu(telefon)
        if vysledek:
            for pojisteny in vysledek:
                print(pojisteny)
        else:
            print("Nenalezen žádný záznam.")

    elif volba == "6":
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vysledek = pojistenci.hledej_podle_jmena_prijmeni(jmeno, prijmeni)
        if vysledek:
            for pojisteny in vysledek:
                print(pojisteny)
        else:
            print("Nenalezen žádný záznam.")

    elif volba == "7":
        vysledek = pojistenci.vypis_vsechny()
        print(vysledek)

        #tady dodělat funkci pro hledání všech pojištěných

    else:
        print("Výběr není platný, zkuste znovu.")
        continue






