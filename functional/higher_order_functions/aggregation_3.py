def aggregation_temp(func, sequence: list, initial=None):
    lst = [func(sequence[0], sequence[1])]
    for i in sequence[2::]:
        lst.append(func(lst[-1], i))
    return initial + int(lst[-1]) if initial is not None else int(lst[-1])


from functools import reduce


def aggregation(func, sequence: list, initial=None):
    if initial is not None:
        result = initial
        start_index = 0
    else:
        result = sequence[0]
        start_index = 1

    for i in sequence[start_index:]:
        result = func(result, i)

    return result


print(aggregation(lambda x, y: x * y, [2, 5, 10, 1, 2], initial = 50))


def get_add(x, y):
    return x + y


print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))
