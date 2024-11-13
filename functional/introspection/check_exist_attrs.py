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


print_goods.is_working = False
print_goods.status = 'Not ready'

print(check_exist_attrs(print_goods, ['is_working', 'status', 'time', 'speed']))
