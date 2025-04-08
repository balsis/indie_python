class Countdown:
    def __init__(self, count):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        return self.count


# Ниже код для проверки методов класса Countdown

count = Countdown(2)

assert hasattr(count, '__next__') is True
assert hasattr(count, '__iter__') is True

iterator = iter(count)
assert next(iterator) == 2
assert next(iterator) == 1
assert next(iterator) == 0
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('Элементы итератора Countdown(7)')
for i in Countdown(7):
    print(i)

print('-' * 10)
print('Элементы итератора Countdown(10)')
for i in Countdown(10):
    print(i)
