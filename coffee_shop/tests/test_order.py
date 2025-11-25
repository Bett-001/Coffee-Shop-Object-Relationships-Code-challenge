from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order
import pytest

def test_order_creation():
    c = Customer("Mike")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 5.5
    with pytest.raises(ValueError):
        Order(c, coffee, 20)
