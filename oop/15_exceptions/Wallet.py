class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif isinstance(currency, str) and len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        elif isinstance(currency, str) and not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        else:
            self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        elif isinstance(other, Wallet) and self.currency != other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance - other.balance)
