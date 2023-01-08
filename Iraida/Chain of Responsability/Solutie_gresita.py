class Material:
    def __init__(self, nume, in_use, pret_expediere):
        self.nume = nume
        self.in_use = in_use
        self.pret_expediere = pret_expediere


class TechnicalCoordinator:
    def aproba_stergere(self, material):
        if not material.in_use:
            print(
                f"Coordonatorul tehnic a aprobat stergerea materialului {material.nume} cu un pret de expediere de {material.pret_expediere}")
        else:
            administrator = Administrator()
            administrator.aproba_stergere(material)


class Administrator:
    def aproba_stergere(self, material):
        print(
            f"Administratorul a aprobat stergerea materialului {material.nume} cu un pret de expediere de {material.pret_expediere}")


material = Material("material1", True, 10.0)
technical_coordinator = TechnicalCoordinator()
technical_coordinator.aproba_stergere(material)
