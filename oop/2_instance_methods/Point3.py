class Point:
    points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.points.append(self)

    def get_distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_distance(self, another_point):
        if not isinstance(another_point, Point):
            print('Передана не точка')
            return None
        return ((self.x - another_point.x) ** 2
                + (self.y - another_point.y) ** 2) ** 0.5

    def display(self):
        print(f"Point({self.x}, {self.y})")
