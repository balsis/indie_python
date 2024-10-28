def is_table_free(table_number: int) -> bool:
    return tables[table_number] is None


def reserve_table(table_number: int, name: str, is_vip: bool) -> None:
    if is_table_free(table_number):
        tables[table_number] = {"name": name, "is_vip": is_vip}


def delete_reservation(table_number):
    tables[table_number] = None

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)