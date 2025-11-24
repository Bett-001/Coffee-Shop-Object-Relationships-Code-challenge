import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_order_validations():
    alice = Customer("Alice")
    latte = Coffee("Latte")

    with pytest.raises(ValueError):
        Order(alice, latte, 0.5)  
    with pytest.raises(ValueError):
        Order(alice, latte, 15.0)  
    with pytest.raises(TypeError):
        Order("NotACustomer", latte, 5.0)
    with pytest.raises(TypeError):
        Order(alice, "NotACoffee", 5.0)
    with pytest.raises(TypeError):
        Order(alice, latte, "NotAPrice")

def test_order_properties():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    order = Order(alice, latte, 5.0)

    assert order.customer == alice
    assert order.coffee == latte
    assert order.price == 5.0
