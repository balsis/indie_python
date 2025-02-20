class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if item in self.values:
            if self.values.count(item) > 1:
                return [i for i, value in enumerate(self.values, 1) if value == item ]
            return self.values.index(item)+1
        else:
            raise ValueError(f'В векторе отсутствует значение {item}')


v1 = Vector(5, 5, 5, 4, 4, 3)
print(v1[4])  # [4, 5]
print(v1[5])  # [1, 2, 3]
print(v1[3])  # 6
try:
    print(v1[2])
except ValueError as e:
    print(e)


