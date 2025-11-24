class Order:
    """
    Order class represents a customer's purchase of a coffee at a certain price.
    Each order links a Customer and a Coffee.
    """
    all_orders = []  # Track all Order instances

    def __init__(self, customer, coffee, price):
        from coffee_shop.customer import Customer
        from coffee_shop.coffee import Coffee

        # Validate inputs
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        """Return the Customer who placed this order"""
        return self._customer

    @property
    def coffee(self):
        """Return the Coffee for this order"""
        return self._coffee

    @property
    def price(self):
        """Return the price of this order"""
        return self._price
