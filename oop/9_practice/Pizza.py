class Pizza:
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

    @classmethod
    def barbecue(cls):
        return cls(['chicken', 'mozzarella', 'red onion', 'sauce bbq'])

    @classmethod
    def peperoni(cls):
        return cls(['mozzarella', 'peperoni', 'tomatoes'])

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])


bbq = Pizza.barbecue()
peperoni = Pizza.peperoni()
margherita = Pizza.margherita()
print(sorted(bbq.ingredients))
print(sorted(peperoni.ingredients))
print(sorted(margherita.ingredients))
