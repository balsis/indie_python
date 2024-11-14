def aggregation(func, sequence: list):
    lst = [func(sequence[0], sequence[1])]
    for i in sequence[2::]:
        lst.append(func(lst[-1], i))
    return lst
def get_add(x, y):
    return x + y


print(aggregation(get_add, [5, 2, 4, 3, 5]))
