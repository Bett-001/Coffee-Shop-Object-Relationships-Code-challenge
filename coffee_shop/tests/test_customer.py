from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
import pytest

def test_customer_name_validation():
    c = Customer("Tom")
    assert c.name == "Tom"
    with pytest.raises(ValueError):
        Customer("")

def test_create_order():
    c = Customer("Anna")
    coffee = Coffee("Mocha")
    order = c.create_order(coffee, 5.0)
    assert order in c.orders()
    assert order in coffee.orders()
