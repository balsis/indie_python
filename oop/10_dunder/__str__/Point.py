class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x={self.x},y={self.y})'

p1 = Point(5, 1)

print(p1)
print(str(p1))