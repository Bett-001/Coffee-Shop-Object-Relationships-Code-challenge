#Coffee Shop Object Relationships

By Tonny Bett

This is a Python object-oriented programming exercise to model a basic coffee shop system. It also helps in practicing to build Python classes that have meaningful relationships with each other. The system has three main classes: Customer, Coffee, and Order. Each class has specific responsibilities and contributes to an overall structure by having customers place orders for specific coffees.

The project includes a full set of tests for confirming your relationships and validations behave as needed.

#Project Structure

Coffee-Shop-Object-Relationships-Code-challenge/
│
├── coffee_shop/
│   ├── customer.py
│   ├── coffee.py
│   ├── order.py
│
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   ├── test_order.py
│   └── __init__.py
│
├── README.md
├── LICENSE


└── debug.py

The coffee_shop folder contains the main class files.

The tests folder contains all pytest tests.

debug.py can be used for testing by hand or for fast experimentation.

#Overview

The system models a simplified version of how a coffee shop works. A customer can have multiple orders; each order is associated with one coffee, and each order maintains a price. With these relationships, the classes can answer such questions as:

Which coffees has a customer tried?

How many customers ordered a particular coffee?

What is the average price of a certain coffee?

How much has a customer spent in total?

This project focuses on clean, readable code and correct object relationships.

Features

#The project supports:

Creating customers with pre-validated names

Creating coffee types with validated names

Creating orders that connect customers and coffees

#Asking for:

All orders of a customer or of a coffee

All the coffees a customer has tried

All customers ordered a certain type of coffee:

Counts of orders

A customer's spending habits

The average price of a coffee


#Class Responsibilities

Customer

Located in: coffee_shop/customer.py

The Customer class represents a single customer.

Responsibilities:

Hold a validated name

Create orders for several coffees

Return all orders associated with the customer

Return all the coffees the customer has ordered

Calculate totals and averages related to spending

Coffee

Located in: coffee_shop/coffee.py

The Coffee class represents a particular type of coffee.

Responsibilities:

Store a validated name

Keep a record of all orders that reference this coffee

Return customers who ordered it

Calculate statistics such as number of orders and average order price

Order

Located in: coffee_shop/order.py

The Order class connects a customer and a coffee.

Responsibilities:

Store references to a customer and a coffee

Check the price

Ensure that the relationship between customer and coffee is recorded correctly.

Each order belongs to exactly one customer and one coffee.

Validations

To guarantee data integrity, observe the following rules:

Customer

*input 'name' must be a string*

Length must be between 1 and 15 characters

Coffee

Name must be a string

Must be at least 3 characters

The name cannot be changed once created.

Order

The price should be a float or integer.

Price must be between 1 and 10

Requires valid Customer and Coffee objects

How the Relationships Work


#The system follows a many-to-many relationship pattern.

Customer  ----<  Order  >----  Coffee

A customer can place several orders:

A coffee may appear in multiple orders.

The order object is the link between both sides.

With these links, each class can make inferences about the others.

Installation


Clone the repository:

git clone https://github.com/your-username/Coffee-Shop-Object-Relationships-Code-challenge.git


cd Coffee-Shop-Object-Relationships-Code-challenge

python3 -m venv venv

source venv/bin/activate


You will only require Python 3-.

Running the Project

python3

Then:

from coffee_shop.customer import Customer

from coffee_shop.coffee import Coffee


from coffee_shop.order import Order

You can also use debug.py to run experiments or quick tests.
Running Tests

The project uses pytest.

To run all tests:

pytest
If everything is implemented correctly, all of these tests should pass.
@Tonny Bett
