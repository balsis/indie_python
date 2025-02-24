class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Напишите реализацию класса Square
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# Ниже располагаются проверки для классов Rectangle и Square

rect_1 = Rectangle(3, 2)
assert rect_1.area() == 6
assert rect_1.perimeter() == 10

rect_2 = Rectangle(10, 5)
assert rect_2.area() == 50
assert rect_2.perimeter() == 30

sq_1 = Square(4)
assert sq_1.area() == 16
assert sq_1.perimeter() == 16

sq_2 = Square(10)
assert sq_2.area() == 100
assert sq_2.perimeter() == 40
print('Good')
