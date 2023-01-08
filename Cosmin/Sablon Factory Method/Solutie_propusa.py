class IChoice:
    def display(self):
        pass


class ComandaClient(IChoice):
    def display(self):
        return "You choose ComandaClient"


class ComandaProductie(IChoice):
    def display(self):
        return "You choose ComandaProductie"


class InvalidChoice(IChoice):
    def display(self):
        return "Invalid choice"


def get_choice_obj(choice: str) -> IChoice:
    obj_choice = None
    if choice.lower() == "comandaclient":
        obj_choice = ComandaClient()
    elif choice.lower() == "comandaproductie":
        obj_choice = ComandaProductie()
    else:
        obj_choice = InvalidChoice()
    return obj_choice


txt_choice = "ComandaClient" # De exemplu cand alegem ComandaClient.
obj_invoice = get_choice_obj(txt_choice)
print(obj_invoice.display())
