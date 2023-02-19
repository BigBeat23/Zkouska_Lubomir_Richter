
class Pojistenci:

    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteny(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def hledej_podle_jmena(self, jmeno):
        return [pojisteny for pojisteny in self.pojisteni if pojisteny.jmeno == jmeno]

    def hledej_podle_prijmeni(self, prijmeni):
        return [pojisteny for pojisteny in self.pojisteni if pojisteny.prijmeni == prijmeni]

    def hledej_podle_vek(self, vek):
        return [pojisteny for pojisteny in self.pojisteni if pojisteny.vek == vek]

    def hledej_podle_telefonu(self, telefon):
        return [pojisteny for pojisteny in self.pojisteni if pojisteny.telefon == telefon]

    def hledej_podle_jmena_prijmeni(self, jmeno, prijmeni):
        return [pojisteny for pojisteny in self.pojisteni if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni]

    def vypis_vsechny(self): #tady dodělat metodu pro výpis všech pojištěných
        for pojisteny in self.pojisteni:
            print(pojisteny.__str__())
pass
