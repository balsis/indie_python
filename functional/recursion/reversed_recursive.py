def reversed_recursive(lst):
    new_lst = []
    for i in reversed(lst):
        if isinstance(i, int):
            new_lst.append(i)
        if isinstance(i, list):
            new_lst.append(reversed_recursive(i))
    return new_lst

print(reversed_recursive([1, 2, 3, 4, 5]))

print(reversed_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
