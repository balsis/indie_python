class Ingredient:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price  # стоимость за 100гр

    @property
    def cost(self):
        return self.weight * self.price / 100


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    @property
    def cost(self):
        summa = 100
        for i in self.ingredients:
            summa += i.cost
        return summa


chicken = Ingredient('chicken', 200, 80)
mozzarella = Ingredient('mozzarella', 300, 110)
sauce_bbq = Ingredient('sauce bbq', 150, 70)
red_onion = Ingredient('red onion', 150, 50)

print('Цена курицы', chicken.cost)
print('Цена моцарелы', mozzarella.cost)
print('Цена соуса', sauce_bbq.cost)
print('Цена красного лука', red_onion.cost)

barbecue = Pizza('BBQ', [chicken, mozzarella, sauce_bbq, red_onion])
print('Стоимость пиццы BBQ', barbecue.cost)
