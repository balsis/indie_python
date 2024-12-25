def power_iter(a: int, n: int) -> int:
    total = 1
    for i in range(n):
        total *= a
    return total


def power(a: int, n: int) -> int:
    if n == 1:
        return a
    if n == 2:
        return a * a
    else:
        return a * power(a, n-1)

print(power(3, 4))

print(power(2, 5))

