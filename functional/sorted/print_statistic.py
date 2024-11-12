def print_statistic(data):
    dct = {}
    for person in data:
        if person[0] in dct:
            dct[person[0]].add(person[1])
        else:
            dct[person[0]] = {person[1]}
    [print(f'Количество уникальных комментаторов у {k} - {len(v)}') for k,v in sorted(dct.items(), key = lambda x: (-len(x[1]), x[0]))]

data = [
    ('karl', 'zhanna777'),
    ('karl', 'мама_игоречка_98'),
    ('qwerty03', 'pushka76'),
    ('Billy', 'мама_игоречка_98'),
    ('Billy', 'pushka76'),
    ('qwerty03', 'joebiden'),
    ('karl', 'zhanna777'),
    ('karl', 'joebiden'),
    ('karl', 'pushka76'),
]

print_statistic(data)