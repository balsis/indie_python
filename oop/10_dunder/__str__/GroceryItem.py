class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'''Name: {self.name}
Price: {self.price}
Quantity: {self.quantity}'''

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'


banana = GroceryItem('Banana', 10, 5)
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
print(str(dragon_fruit))
print(repr(dragon_fruit))