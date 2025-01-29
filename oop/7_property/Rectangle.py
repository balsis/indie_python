class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2*(self.length + self.width)



r1 = Rectangle(5, 10)
print(r1.area)
print(r1.perimeter)
print(isinstance(type(r1).area, property))
print(isinstance(type(r1).perimeter, property))




