def is_table_free(table_number: int) -> bool:
    return tables[table_number] is None


def reserve_table(table_number: int, name: str, is_vip: bool = False) -> None:
    if is_table_free(table_number):
        tables[table_number] = {"name": name, "is_vip": is_vip}


tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: {'name': 'Misha', 'is_vip': False},
}
print(tables)
reserve_table(2, 'Niko', True)
reserve_table(6, 'Chubaka') # не передается вип-статус
print(tables)