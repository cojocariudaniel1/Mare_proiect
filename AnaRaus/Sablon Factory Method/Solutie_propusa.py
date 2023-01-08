class IChoice:
    def display(self):
        pass


class Stock(IChoice):
    def display(self):
        return " You choose Stock"


class Inspectie(IChoice):
    def display(self):
        return "You choose Inspectie"


class Rebut(IChoice):
    def display(self):
        return "You choose Rebut"


class Blocat(IChoice):
    def display(self):
        return "You choose Blocat"


class InvalidChoice(IChoice):
    def display(self):
        return "Invalid choice"


def get_choice_obj(choice: str) -> IChoice:
    obj_choice = None
    if choice.lower() == "stock":
        obj_choice = Stock()
    elif choice.lower() == "inspectie":
        obj_choice = Inspectie()
    elif choice.lower() == "rebut":
        obj_choice = Rebut()
    elif choice.lower() == "blocat":
        obj_choice = Blocat()
    else:
        obj_choice = InvalidChoice()
    return obj_choice


txt_choice = "blocat"
obj_invoice = get_choice_obj(txt_choice.strip())
print(obj_invoice.display())
