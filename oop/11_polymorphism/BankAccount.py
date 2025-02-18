from functools import total_ordering


@total_ordering
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        elif isinstance(other, (int, float)):
            return self.balance == other
        return NotImplemented

    def __lt__(self, other):  # <
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        elif isinstance(other, (int, float)):
            return self.balance < other
        return NotImplemented


values = [BankAccount('Petrovich', 400), 500, BankAccount('Andrey', 200), 100, BankAccount('Zina', 150)]
values.sort()
print(*values)
