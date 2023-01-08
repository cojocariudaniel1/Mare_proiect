from abc import ABC, abstractmethod


class ModCalculPret(ABC):
    @abstractmethod
    def calculare_pret(self, produs):
        pass


class PretFix(ModCalculPret):
    def calculare_pret(self, produs):
        return produs.pret_fix


class PretReteta(ModCalculPret):
    def calculare_pret(self, produs):
        total = 0
        for materie_prima, cantitate in produs.reteta.items():
            total += materie_prima.calculare_pret() * cantitate
        return total


class MateriePrima:
    def __init__(self, nume, cantiate, unitate_masura, pret_unitate):
        self.nume = nume
        self.cantitate = cantiate
        self.unitate_masura = unitate_masura
        self.pret_unitate = pret_unitate

    def calculare_pret(self):
        return self.cantitate * self.pret_unitate


class Produs:
    def __init__(self, nume, reteta, mod_calcul_pret, pret_fix=0):
        self.nume = nume
        self.reteta = reteta
        self.mod_calcul_pret = mod_calcul_pret
        self.pret_fix = pret_fix

    def calculare_productie(self, comanda):
        productie = {}

        for produs, cantitate in comanda.items():
            productie[produs] = cantitate * self.mod_calcul_pret.calculare_pret(self)
        return productie


faina = MateriePrima("Faina", 100, "grame", 2)
zahar = MateriePrima("Zahar", 50, "grame", 3)
cacao = MateriePrima("Cacao", 30, "grame", 4)
lapte = MateriePrima("Lapte", 150, "grame", 2)

reteta_tort = {
    faina: 3,
    zahar: 1,
    cacao: 2}

tort = Produs("Tort cu ciocolata", reteta_tort, PretReteta())
comanda = {tort: 10}
productie = tort.calculare_productie(comanda)
print(
    f"Productie finala {productie.values()}")  # Dict type inseamna ca poate sa aiba mai multe valori, ex: mai multe comenzi

print("Folosim metoda pret Fix")
tort_2 = Produs("Tort cu frisca", reteta_tort, PretFix(), 500)
comanda = {tort: 10}
productie = tort_2.calculare_productie(comanda)
print(f"Folosind metoda de calcul PretFix, pretul comenzii este: {productie.values()}")
