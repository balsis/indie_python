class NamedDuck:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __len__(self):
        return len(str(self))


ducks = [NamedDuck('Amazing'), 'OK', NamedDuck('Lucky'), 'SuperGood', NamedDuck('Zina')]
ducks.sort(key=len, reverse=True)
print([str(x) for x in ducks])