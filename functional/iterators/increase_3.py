def increase_3(lst):
    return tuple(map(lambda x: x * 3, lst))


numbers = [16, -1, 8, 6, -5, -9, 22, 26, 7, -10]
print(increase_3(numbers))
