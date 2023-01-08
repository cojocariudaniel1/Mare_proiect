class Produs:
    def __init__(self, nume, materie_prima, pret=0, ):
        self.nume = nume
        self.materie_prima = materie_prima
        self.pret = pret

    def calculare_pret(self):
        for row in self.materie_prima:
            cantitate = row[1]
            pret_unitate = row[3]
            pret_material_pe_cantitate = cantitate * pret_unitate
            self.pret = self.pret + pret_material_pe_cantitate

    def display(self):
        print(f"Pretul produsului dupa calculare este: {self.pret}")


materiale = [
    ["lapte", 100, "ml", 2],
    ["zahar", 25, "ml", 5],
    ["cacao", 15, "ml", 10]
]
ciocolata = Produs("Ciocolata", materiale)
ciocolata.calculare_pret()
ciocolata.display()
