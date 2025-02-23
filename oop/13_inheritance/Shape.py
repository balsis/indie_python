class Shape:
    pass


class Polygon(Shape):
    pass


class Ellipse(Shape):
    pass


class Triangle(Polygon):
    pass


class Rectangle(Polygon):
    pass


class Circle(Ellipse):
    pass


class Square(Rectangle):
    pass


# Ниже располагаются проверки

assert issubclass(Ellipse, Shape), "Класс Ellipse должен наследоваться от Shape"
assert issubclass(Polygon, Shape), "Класс Polygon должен наследоваться от Shape"

assert issubclass(Circle, Shape), "Класс Circle должен наследоваться от Shape"
assert issubclass(Circle, Ellipse), "Класс Circle должен наследоваться от Ellipse"
assert not issubclass(Circle, Polygon), "Класс Circle не должен наследоваться от Polygon"

assert issubclass(Triangle, Polygon), "Класс Triangle должен наследоваться от Polygon"
assert issubclass(Triangle, Shape), "Класс Triangle должен наследоваться от Shape"
assert not issubclass(Triangle, Ellipse), "Класс Triangle не должен наследоваться от Ellipse"

assert issubclass(Square, Rectangle), "Класс Square должен наследоваться от Rectangle"
assert issubclass(Square, Polygon), "Класс Square должен наследоваться от Polygon"
assert issubclass(Square, Shape), "Класс Square должен наследоваться от Shape"
assert not issubclass(Square, Ellipse), "Класс Square не должен наследоваться от Ellipse"
print('Good')