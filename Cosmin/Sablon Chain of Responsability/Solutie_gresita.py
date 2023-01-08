class OrderApprover:
    def __init__(self):
        pass

    def approve_order(self, order: "Order"):
        if order.price <= 100000:
            print(f"Order price of {order.price} approved by the ResponsabilGestionar")
        elif order.price <= 250000:
            print(f"Order price of {order.price} approved by the SefProductie")
        else:
            print(f"Order price of {order.price} approved by the Administrator")


class Order:
    def __init__(self, price: int):
        self.price = price


def main():
    approver = OrderApprover()
    approver.approve_order(Order(50000))
    approver.approve_order(Order(200000))
    approver.approve_order(Order(500000))


main()
