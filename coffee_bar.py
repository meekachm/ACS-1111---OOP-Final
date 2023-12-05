from person import Order

class CoffeeBar:
    def __init__(self, name, barista):
        self.name = name
        self.orders_list = []
        self.receipts = []
        self.register = 0
        self.tip_jar = 0
        self.barista = barista

    def place_order(self, order):
        self.orders_list.append(order)

    def process_orders(self):
        for order in self.orders_list:
            total_cost = order.price + order.tip
            self.barista.wallet += order.tip
            order.person.wallet -= order.price
            self.register += total_cost
            self.tip_jar += order.tip
            self.receipts.append(order)
            print(f"{self.barista.greeting} {order.to_string()}")
        self.orders_list = []

    def cash_out(self):
        print(f"Amount in the register: {self.register}")

    def cash_out_tips(self):
        self.barista.wallet += self.tip_jar
        self.tip_jar = 0