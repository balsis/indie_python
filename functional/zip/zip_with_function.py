def zip_with_function(lst, func):
    return list(map(func, *lst))


def get_sum_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c

print(zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers))
