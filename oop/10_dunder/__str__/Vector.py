class Vector:
    def __init__(self, *args):
        self.numbers = args

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, value):
        self._numbers = [i for i in value if isinstance(i, int) and not isinstance(i, bool)]

    def __str__(self):
        if self.numbers:
            return f'Вектор({", ".join(map(str, sorted(self.numbers)))})'
        return 'Пустой вектор'

v5 = Vector(1, True, False, 5, 2, True, 4)
print(str(v5))