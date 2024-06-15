def create_actor(**kwargs):
    dct = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
         }
    dct.update(kwargs)

    return dct
