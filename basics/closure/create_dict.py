def create_dict():
    count = 0
    dct = {}

    def inner(name):
        nonlocal count
        count += 1
        dct[count] = name
        return dct
    return inner


f_1 = create_dict()
print(f_1('hello'))  # f_1 возвращает {1: 'hello'}
print(f_1(100))  # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3]))  # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}
