tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

menu = ["salad", "soup", "main_dish", "drink", "desert"]


def is_table_free(table_number: int) -> bool:
    return tables[table_number] is None


def reserve_table(table_number: int, name: str, is_vip: bool = False) -> None:
    if is_table_free(table_number):
        tables[table_number] = {"name": name, "is_vip": is_vip, "order": {}}


def make_order(table_number: int, **kwargs):
    for k, v in kwargs.items():
        if k in menu:
            tables[table_number]['order'][k] = v


make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)
assert tables == {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Лапша'}}, 2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': 'Чечевичный', 'salad': 'Цезарь', 'drink': 'Raf', 'main_dish': 'Утка по-пекински', 'desert': 'Трюфель'}}, 3: None, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
