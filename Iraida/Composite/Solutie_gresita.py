class CutieCiocalata:
    def __init__(self):
        self.lista_ciocolate = []

    def add_ciocolata(self, ciocolata):
        self.lista_ciocolate.append(ciocolata)

    def calculare_cost(self):
        total = 0
        for ciocolate in self.lista_ciocolate:
            total += ciocolate.pret
        print(total)


class Ciocolata:
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret


ciocolata1 = Ciocolata("Milka", 10)
ciocolata2 = Ciocolata("Africana", 3)

cutie_ciocolata = CutieCiocalata()
cutie_ciocolata.add_ciocolata(ciocolata1)
cutie_ciocolata.add_ciocolata(ciocolata2)
cutie_ciocolata.calculare_cost()

