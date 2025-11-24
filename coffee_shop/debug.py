from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create some coffees
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Customers create orders
order1 = alice.create_order(latte, 5.5)
order2 = alice.create_order(mocha, 6.0)
order3 = bob.create_order(latte, 4.0)

# Print results
print("Coffees ordered by Alice:", [c.name for c in alice.coffees()])
print("Customers who ordered Latte:", [c.name for c in latte.customers()])
most_aficionado = Customer.most_aficionado(latte)
print("Top customer for Latte:", most_aficionado.name if most_aficionado else "None")
