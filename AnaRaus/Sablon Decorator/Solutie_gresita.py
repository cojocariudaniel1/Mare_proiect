def display_decorator(func):
    def wrapper(self):
        mesaje = {
            "stock": ("Produs in stoc", "green"),
            "inspectie": ("Produs in inspectie", "red"),
            "rebut": ("Produs rebut", "blue"),
            "blocat": ("Produs blocat", "yellow")
        }
        mesaj, culoare = mesaje.get(self.stare_produs, ("Stare produs necunoscuta", "white"))
        print(f"{culoare} {mesaj}")
        func(self)

    return wrapper


class Produs:
    def __init__(self, stare_produs: str = "stock"):
        self.stare_produs = stare_produs

    @display_decorator
    def display(self):
        print("Display Successful")


# Cream un obiect de tip Produs fara a furniza un argument pentru stare_produs
obj = Produs()

# Apelam functia display
obj.display()
