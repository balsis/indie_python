class FibonacciIterator:
    def __init__(self, count):
        self.count = count
        self.index = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        return value


fibonacci_iter = FibonacciIterator(2)
for number in fibonacci_iter:
    print(number)
