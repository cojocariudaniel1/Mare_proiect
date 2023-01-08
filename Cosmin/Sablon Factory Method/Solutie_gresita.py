choice = "ComandaClient"  # De exemplu


class ComandaClient:
    def display(self):
        print("You choose ComandaClient")


class ComandaProductie:
    def display(self):
        print("You choose ComandaProductie")


if choice == "ComandaClient":
    c = ComandaClient()
    c.display()
elif choice == "ComandaProductie":
    b = ComandaProductie()
    b.display()
