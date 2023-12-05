class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink

    def my_order(self):
        return Order(self, self.favorite_drink)

class Order:
    def __init__(self, person, drink_type):
        self.person = person
        self.drink_type = drink_type

    def to_string(self):
        return f"{self.person.name} orders: {self.drink_type}"

class CoffeeBar:
    def __init__(self, name, barista):
        self.name = name
        self.orders_list = []
        self.barista = barista

    def place_order(self, order):
        self.orders_list.append(order)

    def process_orders(self):
        for order in self.orders_list:
            print(f"{self.barista.greeting} {order.to_string()}")

class Barista(Person):
    def __init__(self, name, favorite_drink, greeting):
        super().__init__(name, favorite_drink)
        self.greeting = greeting

# Creating instances of Person class with different names and favorite drinks
amy = Person("Amy", "Coffee")
bob = Person("Bob", "Tea")
cat = Person("Cat", "Milk")

# Creating an instance of Barista named Kevin
kevin = Barista("Kevin", "Espresso", "Hey dude!")

# Creating an instande of CoffeeBar with a Barista
my_coffee_bar = CoffeeBar("MyCoffeePlace", kevin)

# Assigning Barista Keving to the coffee bar
my_coffee_bar.barista = kevin

# Each customers places an order at the coffee bar
my_coffee_bar.place_order(amy.my_order())
my_coffee_bar.place_order(bob.my_order())
my_coffee_bar.place_order(cat.my_order())

# Processing orderes at the coffee bar
my_coffee_bar.process_orders()


