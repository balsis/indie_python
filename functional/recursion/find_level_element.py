def find_level_element(value, lst, j=1):
    for i in lst:
        if isinstance(i, int) and i == value:
            return j
        if isinstance(i, list):
            rec = find_level_element(value, i, j+1)
            if rec != -1:
                return rec
    return -1


print(find_level_element(5, [1, 2, 3, 4, 5, [5]]))
print(find_level_element(5, [1, 2, 3, 4, [[5]], [5]]))
print(find_level_element(9, [1, 2, 3, 4, [[5]], [5]]))


def is_member(value, lst):
    for i in lst:
        if isinstance(i, int) and i == value:
            return True
        if isinstance(i, list):
            return is_member(value, i)
    return False
