import abc


class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def creaza_gust(self):
        pass

    @abc.abstractmethod
    def creaza_aroma(self):
        pass


class ConcretaFactory1(AbstractFactory):
    def creaza_gust(self):
        return Gust_A1()

    def creaza_aroma(self):
        return Aroma_B1()


class ConcretaFactory2(AbstractFactory):
    def creaza_gust(self):
        return Gust_A2()

    def creaza_aroma(self):
        return Aroma_B2()


class GustAbstract(abc.ABC):
    def interfata_gust(self):
        pass


class AromaAbstract(abc.ABC):
    def interfata_aroma(self):
        pass


class Gust_A1(GustAbstract):
    def interfata_gust(self) -> str:
        return "GustA1"


class Gust_A2(GustAbstract):
    def interfata_gust(self) -> str:
        return "GustA2"


class Aroma_B1(AromaAbstract):
    def interface_aroma(self) -> str:
        return "Aroma_B1"


class Aroma_B2(AromaAbstract):
    def interface_aroma(self) -> str:
        return "Aroma_B2"


class Produs:
    def __init__(self, nume, factory: AbstractFactory):
        self.nume = nume
        self.gust = factory.creaza_gust()
        self.aroma = factory.creaza_aroma()

    def display(self):
        return f"Produsul cu numele {self.nume} are gustul {self.gust} si aroma {self.aroma}"


def main() -> None:
    for fabrica in (ConcretaFactory1(), ConcretaFactory2()):
        aroma = fabrica.creaza_aroma()
        gust = fabrica.creaza_gust()
        print(f"")
        print(f"{aroma.interface_aroma()} {gust.interfata_gust()}")

    factory = ConcretaFactory1()
    ciocolata = Produs("Ciocolata", factory)
    ciocolata.display()


if __name__ == "__main__":
    main()
