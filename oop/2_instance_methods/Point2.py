class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to_origin(self):
        if hasattr(self, "x") and hasattr(self, "y"):
            return ((self.x - 0) ** 2 + (self.y - 0) ** 2) ** 0.5
        else:
            return None

    def display(self):
        if hasattr(self, "x") and hasattr(self, "y"):
            print(f"Point({self.x}, {self.y})")
        else:
            print('Координаты не заданы')

p1 = Point()
p1.set_coordinates(6, 8)
p1.display()
print(p1.get_distance_to_origin())
print()
p2 = Point()
p2.display()
p2.set_coordinates(3, 4)
p2.display()
print(p2.get_distance_to_origin())
print()
p3 = Point()
p3.display()
print(p3.get_distance_to_origin())
p3.x = 4
p3.display()
print(p3.get_distance_to_origin())
p3.y = 3
p3.display()
print(p3.get_distance_to_origin())