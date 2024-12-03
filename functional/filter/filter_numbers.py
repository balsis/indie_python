def filter_numbers(lst):
    return list(filter(lambda x: abs(x) > 100 or x % 2 == 0, lst))


numbers = [-100, 2, -300, -400, 5, -60, -61, -101, 101]
print(filter_numbers(numbers))