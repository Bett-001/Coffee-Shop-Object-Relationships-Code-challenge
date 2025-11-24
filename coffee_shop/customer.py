from coffee_shop.order import Order

class Customer:
    """
    Customer class represents a coffee shop customer.
    Each customer has a name, and can place multiple orders.
    """
    all_customers = []  # Track all Customer instances

    def __init__(self, name):
        self.name = name  
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Validate the customer name
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        """Return all orders placed by this customer"""
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        """Return all unique coffees this customer has ordered"""
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        """Create a new order for this customer"""
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Return the customer who spent the most money on a specific coffee.
        Returns None if no one ordered the coffee.
        """
        customer_totals = {}
        for customer in cls.all_customers:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > 0:
                customer_totals[customer] = total
        if not customer_totals:
            return None
        return max(customer_totals, key=customer_totals.get)
