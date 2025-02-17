class Quadrilateral:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width or length

    def __str__(self):
        if self.length == self.width:
            return f'Квадрат размером {self.length}х{self.width}'
        else:
            return f'Прямоугольник размером {self.length}х{self.width}'

    def __bool__(self):
        return True if self.length == self.width else False


q1 = Quadrilateral(10)
print(q1)
print(bool(q1))
print(isinstance(q1, Quadrilateral))


q2 = Quadrilateral(3, 5)
print(q2)
print(bool(q2))

q3 = Quadrilateral(4, 7)
print(q3)
print(bool(q3))