import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_coffee_name_validation():
    # Coffee name must be a string >= 3 characters
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("aa")

def test_coffee_orders_and_customers():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")

    o1 = alice.create_order(latte, 5.0)
    o2 = bob.create_order(latte, 6.0)

    # Orders and customers returned correctly
    assert set(latte.orders()) == {o1, o2}
    assert set(latte.customers()) == {alice, bob}

def test_num_orders_and_average_price():
    mocha = Coffee("Mocha")
    alice = Customer("Alice")
    
    alice.create_order(mocha, 4.0)
    alice.create_order(mocha, 6.0)

    assert mocha.num_orders() == 2
    assert mocha.average_price() == 5.0
