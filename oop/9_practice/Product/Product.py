class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.balance = self.balance + value

    def is_money_enough(self, value):
        return value <= self.balance

    def payment(self, value):
        if self.is_money_enough(value):
            self.balance = self.balance - value
        else:
            print('Не хватает средств на балансе. Пополните счет')





billy = User('billy@rambler.ru')
print(billy)
print(billy.is_money_enough(350))
billy.deposit(100)
billy.deposit(300)
print(billy.is_money_enough(350))
print(billy)
billy.payment(500)
billy.payment(150)
print(billy)
print()
jack = User('jack@gmail.ru', 800)
print(jack)
print(jack.balance)
jack.payment(600)
jack.payment(200)
jack.payment(1)
jack.balance = 1
jack.payment(1)
print(jack)