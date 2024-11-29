class Point:

    lst = []

    def __init__(self, x=0, y=0):
        self.move_to(x, y)
        Point.lst.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Координаты x = {self.x} и y = {self.y}')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Не принадлежит классу "Точка"')
        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5


p1 = Point(6, 8)
p2 = Point(0, 8)

print(p1.calc_distance(p2))
