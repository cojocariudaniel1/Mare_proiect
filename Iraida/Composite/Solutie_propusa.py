class CutieCiocolata:
    def __init__(self):
        self.children = []

    def add_ciocolata(self, ciocolata):
        self.children.append(ciocolata)

    def remove_ciocolata(self, ciocolata):
        self.children.remove(ciocolata)

    def get_children(self):
        return self.children

    def calculare_cost(self):
        total = 0
        for ciocolata in self.children:
            total += ciocolata.pret
        return total


class Ciocolata:
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret
        self.children = []

    def add_ciocolata(self, ciocolata):
        self.children.append(ciocolata)

    def remove_ciocolata(self, ciocolata):
        self.children.remove(ciocolata)

    def get_children(self):
        return self.children


# Cream o cutie de ciocolată și două ciocolate
cutie = CutieCiocolata()
ciocolata1 = Ciocolata("Dark chocolate", 10)
ciocolata2 = Ciocolata("Milk chocolate", 8)

# Adăugăm ciocolatele în cutie
cutie.add_ciocolata(ciocolata1)
cutie.add_ciocolata(ciocolata2)

# Calculăm costul total al cutiei
cost = cutie.calculare_cost()
print(cost)  # Afișează: 18

# Eliminăm una dintre ciocolate din cutie
cutie.remove_ciocolata(ciocolata1)

# Calculăm din nou costul total al cutiei
cost = cutie.calculare_cost()
print(cost)  # Afișează: 8
