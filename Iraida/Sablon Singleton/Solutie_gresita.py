class Comanda:
    def __init__(self, stare):
        self.stare = stare

    def afiseaza_starea(self):
        print("Starea comenzii este:", self.stare)


# cream un obiect Comanda cu stare "procesată"
comanda1 = Comanda("procesată")
comanda2 = Comanda("neprocesata")
# afișăm starea comenzii
comanda1.afiseaza_starea()  # afișează "Starea comenzii este: procesată"
comanda2.afiseaza_starea()  # afișează "Starea comenzii este: procesată"
