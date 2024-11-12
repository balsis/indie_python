def print_order_rating(drivers_list):
    dct = {}
    for driver in drivers_list:
        if driver[0] in dct:
            dct[driver[0]].append(driver[1])
        else:
            dct[driver[0]] = [driver[1]]
    lst = [(k, sum(v) / len(v)) for k, v in dct.items()]
    [print(f'{i[0]} {i[1]}') for i in sorted(lst, key = lambda x: (-x[1], x[0].upper()))]


drivers = [
    ('Джек', 2),
    ('Джек', 3),
    ('Гермиона', 5),
    ('Билл', 4),
    ('Билл', 4),
    ('Гермиона', 3),
    ('Джек', 2),
    ('ЯЯ', 5),
    ('ФФФ', 5),
    ('Билл', 4),
    ('Укк', 4),
    ('Билл', 3),
    ('Джек', 2),
    ('Джек', 2),
    ('Гермиона', 5),
    ('Билл', 2),
    ('ФФФ', 4),
    ('Билл', 3),
    ('ФФФ', 3),
    ('Джек', 2),
    ('Джек', 1),
    ('Гермиона', 5),
    ('Билл', 2),
    ('Курт', 5),
    ('Билл', 3),
]
print_order_rating(drivers)
