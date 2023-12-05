from person import Person, Barista
from coffee_bar import CoffeeBar

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
