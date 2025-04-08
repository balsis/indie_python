class SequenceIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
