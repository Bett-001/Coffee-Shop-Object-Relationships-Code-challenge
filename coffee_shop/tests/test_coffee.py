from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer

def test_coffee_orders_and_customers():
    coffee = Coffee("Cappuccino")
    c1 = Customer("Tom")
    c2 = Customer("Ann")
    c1.create_order(coffee, 4.0)
    c2.create_order(coffee, 5.0)
    assert coffee.num_orders() == 2
    assert set(c.name for c in coffee.customers()) == {"Tom", "Ann"}
    assert coffee.average_price() == 4.5
