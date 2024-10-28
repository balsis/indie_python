def product(lst: list, start: int = 1) -> int:
    result = start
    for i in lst:
        result *= i
    return result


print(product([1, 2, 3]))
print(product([1, 2, 3], start = 10))
