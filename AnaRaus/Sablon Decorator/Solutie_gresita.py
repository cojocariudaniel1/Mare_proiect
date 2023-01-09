class Produs:
    def __init__(self, stare_produs: str = "stock"):
        self.stare_produs = stare_produs

    def display(self):
        mesaje = {
            "stock": ("Produsul este in stoc", "green"),
            "inspectie": ("Produsul este in curs de inspectie", "yellow"),
            "rebut": ("Produsul este rebut", "red"),
            "blocat": ("Produsul este blocat", "blue"),
        }
        mesaj, culoare = mesaje.get(self.stare_produs, ("Stare produs necunoscuta", "white"))
        print(f"{culoare} {mesaj}")
        print("Display Successful")


# Cream un obiect de tip Produs fara a furniza un argument pentru stare_produs
obj = Produs()

# Apelam functia display
obj.display()
