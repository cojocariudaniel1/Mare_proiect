from abc import ABC, abstractmethod


class Material(ABC):
    def __init__(self, nume, in_use, pret_expediere):
        self.nume = nume
        self.in_use = in_use
        self.pret_expediere = pret_expediere
        self.successor = None

    @abstractmethod
    def aproba_stergere(self):
        pass

    def set_successor(self, successor):
        self.successor = successor

    def handle_aproba_stergere(self):
        result = self.aproba_stergere()
        if not result and self.successor is not None:
            self.successor.handle_aproba_stergere()


class TechnicalCoordinator(Material):
    def aproba_stergere(self):
        if not self.in_use:
            print(
                f"Coordonatorul tehnic a aprobat stergerea materialului {self.nume} cu un pret de expediere de {self.pret_expediere}")
            return True
        return False


class Administrator(Material):
    def aproba_stergere(self):
        print(
            f"Administratorul a aprobat stergerea materialului {self.nume} cu un pret de expediere de {self.pret_expediere}")
        return True


technical_coordinator = TechnicalCoordinator("Widget", True, 10.0)
administrator = Administrator("Widget", True, 10.0)

# Setează TechnicalCoordinator ca următorul obiect în lanțul de responsabilitate după material
technical_coordinator.set_successor(administrator)

# Încearcă să aprobe ștergerea materialului
technical_coordinator.handle_aproba_stergere()

technical_coordinator1 = TechnicalCoordinator("Material2", False, 150.0)
technical_coordinator1.handle_aproba_stergere()
