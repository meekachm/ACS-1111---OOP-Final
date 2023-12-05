class Person:
    def __init__(self, name, favorite_drink, wallet, tip_amount):
        self.name = name
        self.favorite_drink = favorite_drink
        self.wallet = wallet
        self.tip_amount = tip_amount

    def my_order(self, price):
        tip = price * self.tip_amount
        return Order(self, self.favorite_drink, price, tip)

class Order:
    def __init__(self, person, drink_type, price, tip):
        self.person = person
        self.drink_type = drink_type
        self.price = price
        self.tip = tip

    def to_string(self):
        return f"{self.person.name} orders: {self.drink_type}, Total Cost: {self.price + self.tip}"

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

class Barista(Person):
    def __init__(self, name, favorite_drink, greeting, wallet, tip_amount):
        super().__init__(name, favorite_drink, wallet, tip_amount)
        self.greeting = greeting

# Instances of different customer and their favorite drinks
amy = Person("Amy", "Coffee", 52.5, 0.2)
bob = Person("Bob", "Tea", 74.15, 0.18)
cat = Person("Cat", "Milk", 23.5, 0.15)

# Instance of Barista named Kevin
kevin = Barista("Kevin", "Espresso", "Hey dude!", 0.0, 0.0)

# Instance of CoffeeBar with a Barista
my_coffee_bar = CoffeeBar("MyCoffeePlace", kevin)

# Assigning Barista Kevin
my_coffee_bar.barista = kevin

# Each customer's order with their cost of order
order_amy = amy.my_order(8.5)
order_bob = bob.my_order(12.0)
order_cat = cat.my_order(2.5)

# Each customers places an order 
my_coffee_bar.place_order(order_amy)
my_coffee_bar.place_order(order_bob)
my_coffee_bar.place_order(order_cat)

# Processing orderes
my_coffee_bar.process_orders()

# Displaying the amount in the register and cash out tips
my_coffee_bar.cash_out()
my_coffee_bar.cash_out_tips()
