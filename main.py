class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink

    def my_order(self):

class Order:
    def __init__(self, person, drink_type):
        self.person = person
        self.drink_type = drink_type

    def to_string(self):
        return f"{self.person.name} orders: {self.drink_type}"


