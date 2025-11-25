from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")

espresso = Coffee("Espresso")
latte = Coffee("Latte")

c1.create_order(espresso, 5.0)
c1.create_order(latte, 6.5)
c2.create_order(espresso, 4.5)

print("Alice coffees:", [c.name for c in c1.coffees()])
print("Espresso customers:", [c.name for c in espresso.customers()])
print("Espresso avg price:", espresso.average_price())
