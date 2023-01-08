class MateriePrima:
    def __init__(self, nume, cantiate, unitate_masura, pret_unitate):
        self.nume = nume
        self.cantitate = cantiate
        self.unitate_masura = unitate_masura
        self.pret_unitate = pret_unitate

    def calculare_pret(self):
        return self.cantitate * self.pret_unitate


class Produs:
    def __init__(self, nume, reteta, ):
        self.nume = nume
        self.reteta = reteta

    def calculare_productie(self, comanda):
        productie = {}

        for produs, cantiate in comanda.items():
            productie[produs] = cantiate * self.calcuare_pret()

        return productie

    def calcuare_pret(self):
        total = 0
        for materie_prima, cantitate in self.reteta.items():
            total += materie_prima.calculare_pret() * cantitate

        return total


faina = MateriePrima("Faina", 100, "grame", 2)
zahar = MateriePrima("Zahar", 50, "grame", 3)
cacao = MateriePrima("Cacao", 30, "grame", 4)
lapte = MateriePrima("Lapte", 150, "grame", 2)

reteta_tort = {
    faina: 3,
    zahar: 1,
    cacao: 2}

tort = Produs("Tort cu ciocolata", reteta_tort)
comanda = {tort: 1}
productie = tort.calculare_productie(comanda)
print(f"Productie finala {productie.values()}")
