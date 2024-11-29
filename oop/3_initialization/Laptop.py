# Напишите определение класса Laptop
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

laptop1 = Laptop('HP', 'z679', 5500)
laptop2 = Laptop('LG', 'u689', 5000)
# Ниже код для проверки класса Laptop и ЭК laptop1 и laptop2


assert isinstance(laptop1, Laptop)
assert isinstance(laptop2, Laptop)

hp = Laptop('hp', '15-bw0xx', 57000)
assert hp.laptop_name == 'hp 15-bw0xx'
assert hp.price == 57000
assert isinstance(hp, Laptop)

lenovo = Laptop('lenovo', 'z-570-dx', 61000)
assert lenovo.brand == 'lenovo'
assert lenovo.model == 'z-570-dx'
assert lenovo.price == 61000
assert lenovo.laptop_name == 'lenovo z-570-dx'
assert isinstance(lenovo, Laptop)
print('Good')
