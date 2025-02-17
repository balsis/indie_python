from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.height * self.width

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return True if self.area == other else False
        elif isinstance(other, Rectangle):
            return True if self.area == other.area else False
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):  # >
        if isinstance(other, (int, float)):
            return True if self.area > other else False
        elif isinstance(other, Rectangle):
            return True if self.area > other.area else False
        else:
            return 'Невозможно выполнить сравнение'

# Ниже код для проверки методов класса Rectangle

r1 = Rectangle(3, 4)
assert r1.width == 3
assert r1.height == 4
assert r1.area == 12
assert isinstance(type(r1).area, property), 'Вы не создали property area'

assert r1 > 11
assert not r1 > 12
assert r1 >= 12
assert r1 <= 12
assert not r1 > 13
assert not r1 == 13
assert r1 != 13
assert r1 == 12

r2 = Rectangle(2, 6)
assert r1 == r2
assert not r1 != r2
assert not r1 > r2
assert not r1 < r2
assert r1 >= r2
assert r1 <= r2

r3 = Rectangle(5, 2)
assert not r2 == r3
assert r2 != r3
assert r2 > r3
assert not r2 < r3
assert r2 >= r3
assert not r2 <= r3
print('Good')