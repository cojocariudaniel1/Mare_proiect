class Comanda:
    _instance = None

    def __init__(self, stare):
        if Comanda._instance is not None:
            raise Exception(
                "Această clasă este un singleton. Utilizați Comanda.get_instance() pentru a obține instanța.")
        self.stare = stare

    @classmethod
    def get_instance(cls, stare=None):
        if cls._instance is None:
            cls._instance = Comanda(stare)
        return cls._instance

    def afiseaza_starea(self):
        print("Starea comenzii este:", self.stare)


# încercăm să cream o instanță prin apelarea metodei de inițializare direct
try:
    comanda = Comanda("procesată")
except Exception as e:
    print(e)  # afișează "Această clasă este un singleton. Utilizați Comanda.get_instance() pentru a obține instanța."

# obținem instanța prin apelarea metodei de clasă get_instance()
comanda = Comanda.get_instance("procesată")
comanda.afiseaza_starea()  # afișează "Starea comenzii este: procesată"

# încercăm să cream o altă instanță prin apelarea metodei de inițializare direct
try:
    comanda_2 = Comanda("prelucrată")
except Exception as e:
    print(e)  # afișează "Această clasă este un singleton. Utilizați Comanda.get_instance() pentru a obține instanța."

# obținem aceeași instanță prin apelarea metodei de clasă get_instance() fără a specifica o stare
comanda_2 = Comanda.get_instance()
comanda_2.afiseaza_starea()  # afișează "Starea comenzii este: procesată"

# modificăm starea prin accesarea atributului stare direct
comanda_2.stare = "prelucrată"
comanda.afiseaza_starea()  # afișează "Starea comenzii este: prelucrată"
