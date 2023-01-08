def display_decorator(func):
    def wrapper(self):
        mesaje = {
            "procesata": ("Comanda procesata", "green"),
            "anulata": ("Comanda anulata", "red"),
            "acceptata": ("Comanda acceptata", "blue"),
            "in lucru": ("Comanda in lucru", "yellow"),
            "finalizata": ("Comanda finalizata", "purple")
        }
        mesaj, culoare = mesaje.get(self.stare_comanda, ("Stare comanda necunoscuta", "white"))
        print(f"{culoare} {mesaj}")
        func(self)

    return wrapper


class ComandaClient:
    def __init__(self, stare_comanda: str = "procesata"):
        self.stare_comanda = stare_comanda

    @display_decorator
    def display(self):
        print("Display Successful")


# Cream un obiect de tip ComandaClient fara a furniza un argument pentru stare_comanda
obj = ComandaClient()

# Apelam functia display
obj.display()