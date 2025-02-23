class MyList(list):
    def remove_all(self, value):
        while value in self:
            self.remove(value)


s = MyList([1, 2, 3, 2, 1, 2])
# Ниже располагаются проверки для класса MyList
s = MyList([1, 2, 3, 2, 1, 2])
assert s == [1, 2, 3, 2, 1, 2]
s.remove_all(2)
assert s == [1, 3, 1]
s.remove_all(1)
assert s == [3]
s.remove_all(5)
assert s == [3]
s.remove_all(3)
assert s == []

k = MyList([0] * 20)
assert k == [0] * 20
k.remove_all(7)
assert k == [0] * 20
k.append(8)
k.append(0)
k.append(2)
k.remove_all(0)
assert k == [8, 2]
print('Good')
