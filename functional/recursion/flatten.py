def flatten(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, int):
            new_lst.append(i)
        elif isinstance(i, list):
            new_lst.extend(flatten(i))
    return new_lst


print(flatten([1, [2, 3, [4]], 5]))


