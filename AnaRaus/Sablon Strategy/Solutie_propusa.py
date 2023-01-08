from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calculeaza_pret(self, cost_produs, cost_ambalaj, cost_transport):
        pass


class AverageStrategy(Strategy):
    def calculeaza_pret(self, cost_produs, cost_ambalaj, cost_transport):
        return (cost_produs + cost_ambalaj + cost_transport) / 3


class StandardStrategy(Strategy):
    def calculeaza_pret(self, cost_produs, cost_ambalaj, cost_transport):
        return cost_produs + cost_ambalaj + cost_transport


class Produs:
    def __init__(self, cost_produs, cost_ambalaj, cost_transport, strategy):
        self.cost_produs = cost_produs
        self.cost_ambalaj = cost_ambalaj
        self.cost_transport = cost_transport
        self.strategy = strategy

    def calculeaza_pret(self):
        return self.strategy.calculeaza_pret(self.cost_produs, self.cost_ambalaj, self.cost_transport)


# Crearea unui obiect de tip Produs cu strategia StandardStrategy
produs = Produs(100, 20, 50, StandardStrategy())

# Calcularea și afișarea prețului final al produsului
pret_produs = produs.calculeaza_pret()
print(pret_produs)

# Crearea unui obiect de tip Produs cu strategia AverageStrategy
produs = Produs(100, 20, 50, AverageStrategy())

# Calcularea și afișarea prețului final al produsului
pret_produs = produs.calculeaza_pret()
print(pret_produs)
