def is_only_one_positive(*args):
    return len([i for i in args if i > 0]) == 1


print(is_only_one_positive())
print(is_only_one_positive(1))
print(is_only_one_positive(-1, 2))
print(is_only_one_positive(-1, -2, -3, -4))
print(is_only_one_positive(-1, -2, -3, 4,-5))
