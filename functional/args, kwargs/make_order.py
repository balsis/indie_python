menu = ["salad", "soup", "main_dish", "drink", "desert"]


def is_table_free(table_number: int) -> bool:
    return tables[table_number] is None


def reserve_table(table_number: int, name: str, is_vip: bool = False) -> None:
    if is_table_free(table_number):
        tables[table_number] = {"name": name, "is_vip": is_vip, "order": {}}


def make_order(table_number: int, **kwargs):
    for k, v in kwargs.items():
        if k in menu:
            if k in tables[table_number]["order"]:
                tables[table_number]["order"][k] += v.split(",")
            else:
                tables[table_number]["order"][k] = v.split(",")


def delete_order(*, number_table: int, delete_all=False, **kwargs):
    if delete_all:
        tables[number_table]['order'] = {}
    else:
        for k, v in kwargs.items():
            if k in menu and v:
                tables[number_table]['order'].pop(k, None)


tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}
make_order(1, soup='Borsh')
make_order(1, soup='Лапша')
print(tables)
