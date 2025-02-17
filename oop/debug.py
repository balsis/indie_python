class MyClass:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x is other.x

a = MyClass([1, 2, 3])
b = MyClass([1, 2, 3])

print(a == b)