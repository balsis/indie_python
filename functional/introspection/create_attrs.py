def create_attrs(obj, lst):
    for i in lst:
        setattr(obj, i[0], i[1])


def check_exist_attrs(obj: object, lst: list):
    dct = {}
    for i in lst:
        if hasattr(obj, i):
            dct[i] = True
        else:
            dct[i] = False
    return dct


def print_goods(lst):
    pass


def print_goods(lst):
    pass

create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])

print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))
