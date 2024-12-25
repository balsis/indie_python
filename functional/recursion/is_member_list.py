def is_member(value, lst):
    for i in lst:
        if isinstance(i, int) and i == value:
            return True
        if isinstance(i, list):
            return is_member(value, i)
    return False


# print(is_member(45, [1, 2, 3, 4, 5]))
print(is_member(9, [1, 2, 3, 4, 5,
                 [6, 7, 8,
                  [9, 1, [2, [3], 4], 5, 6]]]))
