class Pojisteny:

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"Jméno: {self.jmeno} Příjmení: {self.prijmeni} Věk: {self.vek} Telefonní číslo: {self.telefon}"

pass


