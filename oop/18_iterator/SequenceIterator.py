class SequenceIterator:
    def __init__(self, data):
        self.data = data[0::2]+data[1::2]

    def __iter__(self):
        return iter(self.data)


container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
