def get_max_recursive(lst):
    maximum = 0
    for i in lst:
        if isinstance(i, int) and i > maximum:
            maximum = i
        if isinstance(i, list):
            wrap_maximum = get_max_recursive(i)
            if wrap_maximum > maximum:
                maximum = wrap_maximum
    return maximum

# print(get_max_recursive([1, 2, 3, 4, 5]))
# print(get_max_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# print(get_max_recursive([1, 2, 3, 4, [[5]], [5]]))
print(get_max_recursive([1, 2, 3, 4, 5,
                        [6, 7, 8,
                        [[[9]], 1, [2, [3], 4], 5, 6]]]))

