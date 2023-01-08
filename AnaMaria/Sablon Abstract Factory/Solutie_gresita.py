class GustAbstract(object):
    def interfata_gust(self):
        pass


class AromaAbstract(object):
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
    def __init__(self, nume, gust, aroma):
        self.nume = nume
        self.gust = gust
        self.aroma = aroma

    def display(self):
        print(f"Produsul cu numele {self.nume} are gustul {self.gust} si aroma {self.aroma}")


def main() -> None:
    gust1 = Gust_A1()
    aroma1 = Aroma_B1()
    print({aroma1.interface_aroma(), gust1.interfata_gust()})

    gust2 = Gust_A2()
    aroma2 = Aroma_B2()
    print({aroma2.interface_aroma(), gust2.interfata_gust()})


    gust_ciocolata = Gust_A1()
    aroma_ciocolata = Aroma_B1()
    ciocolata = Produs("Ciocolata", gust_ciocolata,aroma_ciocolata)
    ciocolata.display()

if __name__ == "__main__":
    main()
