class Material:
    def __init__(self, nume, cantitate, unitate_masura, pret_unitate):
        self.nume = nume
        self.cantitate = cantitate
        self.unitate_masura = unitate_masura
        self.pret_unitate = pret_unitate

    def calculare_pret(self):
        return self.cantitate * self.pret_unitate


class Produs:
    def __init__(self, nume, materie_prima=None, pret=0, ):
        if materie_prima is None:
            materie_prima = []
        self.nume = nume
        self.materie_prima = materie_prima
        self.pret = pret

    def adaugare_material(self, material):
        self.materie_prima.append(material)

    def eliminare_material(self, material):
        self.materie_prima.remove(material)

    def calculare_pret(self):
        for material in self.materie_prima:
            self.pret += material.calculare_pret()

    def display(self):
        print(f"Pretul produsului dupa calculare este: {self.pret}")


tort = Produs("Tort cu ciocolata")
faina = Material("Faina", 200, "grame", 10)
zahar = Material("Zahar", 10, "grame", 6)
cacao = Material("Cacao", 50, 'grame', 5)

tort.adaugare_material(faina)
tort.adaugare_material(zahar)
tort.adaugare_material(cacao)

tort.calculare_pret()
tort.display()
