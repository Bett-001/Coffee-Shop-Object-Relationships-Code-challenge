import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_customer_name_validation():
    # Name must be a string between 1 and 15 chars
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")  # too short
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLong")  # too long

def test_customer_orders_and_coffees():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")

    # used to Create orders
    o1 = alice.create_order(latte, 5.0)
    o2 = alice.create_order(mocha, 6.0)

    # used to Check orders are returned
    assert o1 in alice.orders()
    assert o2 in alice.orders()

    # used to Check unique coffees returned
    assert set(alice.coffees()) == {latte, mocha}

def test_most_aficionado():
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    espresso = Coffee("Espresso")

    bob.create_order(espresso, 3.0)
    charlie.create_order(espresso, 5.0)

    top_customer = Customer.most_aficionado(espresso)
    assert top_customer == charlie
