from abc import ABC, abstractmethod


class OrderApprover(ABC):
    def __init__(self, next_approver: "OrderApprover" = None):
        self.next_approver = next_approver

    def set_next_approver(self, next_approver: "OrderApprover"):
        self.next_approver = next_approver

    @abstractmethod
    def approve_order(self, order: "Order"):
        pass


class ResponsabilGestionar(OrderApprover):
    def approve_order(self, order: "Order"):
        if order.price <= 100000:
            print(f"Order price of {order.price} approved by the ResponsabilGestionar")
        elif self.next_approver:
            self.next_approver.approve_order(order)


class SefProductie(OrderApprover):
    def approve_order(self, order: "Order"):
        if order.price <= 250000:
            print(f"Order price of {order.price} approved by the SefProductie ")
        elif self.next_approver:
            self.next_approver.approve_order(order)


class Administrator(OrderApprover):
    def approve_order(self, order: "Order"):
        print(f"Order price of {order.price} approved by the Administrator ")


class Order:
    def __init__(self, price: int):
        self.price = price


def main():
    a = ResponsabilGestionar()
    b = SefProductie()
    c = Administrator()
    a.set_next_approver(b)
    b.set_next_approver(c)
    a.approve_order(Order(50000))  # this will be approved by the ResponsabilGestionar
    a.approve_order(Order(200000))  # this will be approved by the SefProductie
    a.approve_order(Order(500000))  # this will be approved by the Administrator


main()
