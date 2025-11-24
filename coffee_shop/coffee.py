from coffee_shop.order import Order

class Coffee:
    """
    Coffee class represents a type of coffee in the shop.
    Each coffee has a name and can be ordered many times by different customers.
    """
    all_coffees = []  # Track all Coffee instances

    def __init__(self, name):
        self.name = name  
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Validate the coffee name
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value

    def orders(self):
        """Return all orders that include this coffee"""
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        """Return all unique customers who have ordered this coffee"""
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        """Return the total number of times this coffee has been ordered"""
        return len(self.orders())

    def average_price(self):
        """Return the average price of this coffee based on its orders"""
        orders_list = self.orders()
        if not orders_list:
            return 0
        return sum(order.price for order in orders_list) / len(orders_list)
