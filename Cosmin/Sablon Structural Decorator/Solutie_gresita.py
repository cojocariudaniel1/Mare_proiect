class ComandaClient:
    def __init__(self, stare_comanda: str = "procesata"):
        self.stare_comanda = stare_comanda

    def display(self):
        mesaje = {
            "procesata": ("Comanda procesata", "green"),
            "anulata": ("Comanda anulata", "red"),
            "acceptata": ("Comanda acceptata", "blue"),
            "in lucru": ("Comanda in lucru", "yellow"),
            "finalizata": ("Comanda finalizata", "purple")
        }
        mesaj, culoare = mesaje.get(self.stare_comanda, ("Stare comanda necunoscuta", "white"))
        print(f"{culoare} {mesaj}")
        print("Display Successful")


# Cream un obiect de tip ComandaClient fara a furniza un argument pentru stare_comanda
obj = ComandaClient()

# Apelam functia display
obj.display()
