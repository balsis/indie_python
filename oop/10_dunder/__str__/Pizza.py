class Ingredient:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}: {self.weight}г.'
class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def __str__(self):
        lst = '\n'.join(str(i) for i in sorted(self.ingredients, key = lambda x: x.weight, reverse = True))
        return f'Пицца {self.name} состоит из:\n{lst}'


barbecue = Pizza('BBQ', [
    Ingredient('chicken', 200),
    Ingredient('mozzarella', 300),
    Ingredient('sauce bbq', 150),
    Ingredient('red onion', 150)
])

print(barbecue)
