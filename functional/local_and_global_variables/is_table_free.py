tables = {
    1: 'Andrey',
    2: None,
    3: None,
    4: None,
    5: 'Vasiliy',
    6: None,
    7: None,
    8: 'Stas',
    9: None,
}


def is_table_free(table_number: int) -> bool:
    return tables[table_number] is None


def get_free_tables():
    free_tables = [table for table, name in tables.items() if name is None]
    return free_tables


print(is_table_free(1))
print(is_table_free(2))
print(get_free_tables())
