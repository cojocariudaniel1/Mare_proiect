class MetodaCalculProdus:
    AVERAGE = "average"
    STANDARD = "standard"


class Produs:
    def __init__(self, cost_produs, cost_ambalaj, cost_transport, metoda_calcul):
        self.cost_produs = cost_produs
        self.cost_ambalaj = cost_ambalaj
        self.cost_transport = cost_transport
        self.metoda_calcul = metoda_calcul

    def calculeaza_pret(self):
        if self.metoda_calcul == MetodaCalculProdus.AVERAGE:
            pret = (self.cost_produs + self.cost_ambalaj + self.cost_transport) / 3
            return pret
        elif self.metoda_calcul == MetodaCalculProdus.STANDARD:
            pret = self.cost_produs + self.cost_ambalaj + self.cost_transport
            return pret


# Crearea unui obiect de tip Produs cu metoda de calcul "standard"
produs = Produs(100, 20, 50, MetodaCalculProdus.STANDARD)

# Calcularea și afișarea prețului final al produsului
pret_produs = produs.calculeaza_pret()
print(pret_produs)

# Crearea unui obiect de tip Produs cu metoda de calcul "average"
produs = Produs(100, 20, 50, MetodaCalculProdus.AVERAGE)

# Calcularea și afișarea prețului final al produsului
pret_produs = produs.calculeaza_pret()
print(pret_produs)
