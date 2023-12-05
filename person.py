class Person:
    def __init__(self, name, favorite_drink, wallet, tip_amount):
        self.name = name
        self.favorite_drink = favorite_drink
        self.wallet = wallet
        self.tip_amount = tip_amount

    def my_order(self, price):
        tip = price * self.tip_amount
        return Order(self, self.favorite_drink, price, tip)
    

class Barista(Person):
    def __init__(self, name, favorite_drink, greeting, wallet, tip_amount):
        super().__init__(name, favorite_drink, wallet, tip_amount)
        self.greeting = greeting


class Order:
    def __init__(self, person, drink_type, price, tip):
        self.person = person
        self.drink_type = drink_type
        self.price = price
        self.tip = tip

    def to_string(self):
        return f"{self.person.name} orders: {self.drink_type}, Total Cost: {self.price + self.tip}"
