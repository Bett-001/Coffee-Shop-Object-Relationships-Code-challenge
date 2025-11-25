class Order:
    def __init__(self, customer, coffee, price):
        from coffee_shop.customer import Customer
        from coffee_shop.coffee import Coffee
        if not isinstance(customer, Customer) or not isinstance(coffee, Coffee):
            raise ValueError("Invalid customer or coffee.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be 1.0-10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
