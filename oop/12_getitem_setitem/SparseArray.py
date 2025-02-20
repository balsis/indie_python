class SparseArray:
    def __init__(self, *args):
        self._values = []
        for i in args:
            self._values.append(i)

    def __len__(self):
        return len(self.values)

    @property
    def values(self):
        return tuple(self._values)

    def __getitem__(self, index):
        if len(self._values) >= index:
            return self._values[index]
        else:
            diff = index - len(self.values) + 1
            self._values.extend([None] * diff)

    def __setitem__(self, index, value):
        if len(self._values) >= index:
            self._values[index] = value
        else:
            diff = index - len(self.values) + 1
            self._values.extend([None] * diff)
            self._values[index] = value

    def __delitem__(self, index):
        if len(self._values) >= index:
            self._values[index] = None


array = SparseArray(1, 2, 3)
print(array.values)
print(array[7])
print(array.values)
array[6] = 100
print(array.values)
array[10] = 200
print(array.values)
del array[1]
print(array.values)
print(len(array))
