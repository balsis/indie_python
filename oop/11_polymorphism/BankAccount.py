class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __radd__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        elif isinstance(other, Numbers):
            return sum(self.balance + value for value in other._values)
        elif isinstance(other, (int, float)):
            return self.balance + other
        return NotImplemented


class Numbers:
    def __init__(self, values: list):
        self._values = values

    def __radd__(self, other):
        if isinstance(other, BankAccount):
            return sum(other.balance + value for value in self._values)
        elif isinstance(other, Numbers):
            return sum(self._values) + sum(other._values)
        elif isinstance(other, (int, float)):
            return sum(self._values) + other
        return NotImplemented


lst = [
    Numbers([10, 20, 10]),
    BankAccount('Ivan', 30),
    Numbers([30, 40]),
]

# Для корректного сложения используем начальное значение 0
result = sum(lst, 0)
print(result)  # Ожидаем 140