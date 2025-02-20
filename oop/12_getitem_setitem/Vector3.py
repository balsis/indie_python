class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 <= item <= len(self.values):
                return self.values[item-1]
            else:
                raise IndexError(f"Индекс {item} находится за пределами вектора")
        if isinstance(item, str):
            if 0 < len(item) <= len(self.values):
                return self.values[len(item)-1]
            else:
                raise IndexError(f"Индекс {len(item)} находится за пределами вектора")

v = Vector(5, 7, 8, 9, 2, 3)
print(v['q'])  # 5
print(v['_+'])  # 7
print(v['567'])  # 8
print(v['!@#$'])  # 9
print(v['abba'])  # 9
print(v['qwerty'])  # 3
try:
    print(v['abracadabra'])
except IndexError as e:
    print(e)
