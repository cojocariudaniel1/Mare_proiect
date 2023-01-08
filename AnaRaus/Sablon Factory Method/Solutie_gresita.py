class ProdusInStoc:
    def display(self):
        print("Produsul este in stoc")


class ProdusInInspectie:
    def display(self):
        print("Produsul este in inspectie")


class ProdusBlocat:
    def display(self):
        print("Produsul este blocat")


class ProdusInRebut:
    def display(self):
        print("Produsul este in rebut")


choice = "ProdusInRebut"  # De exemplu

if choice == "ProdusInStoc":
    a = ProdusInStoc()
    a.display()
elif choice == "ProdusInInspectie":
    b = ProdusInInspectie()
    b.display()
elif choice == "ProdusInRebut":
    c = ProdusInRebut()
    c.display()
elif choice == "ProdusBlocat":
    d = ProdusBlocat()
    d.display()
