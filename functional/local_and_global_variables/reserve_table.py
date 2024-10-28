def is_table_free(table_number: int) -> bool:
    return tables[table_number] is None


def reserve_table(table_number: int, name: str) -> None:
    if is_table_free(table_number):
        tables[table_number] = name


def delete_reservation(table_number):
    tables[table_number] = None


tables = {
    1: 'Andrey',
    2: None,
    3: 'Gena',
    4: 'Artem',
    5: 'Vasiliy',
    6: None,
    7: 'Artur',
    8: None,
    9: 'Misha',
}
print(tables)
delete_reservation(1)
delete_reservation(3)
reserve_table(6, 'Chubaka')
print(tables)
