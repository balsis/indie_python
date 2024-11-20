def create_dict():
    dct = {}
    count = 0

    def inner(value):
        nonlocal count
        count += 1
        dct[count] = value
        return dct

    return inner


f_1 = create_dict()
print(f_1('privet'))
print(f_1('poka'))
print(f_1([5, 2, 3]))

f2 = create_dict()
print(f2(5))
print(f2(15))
