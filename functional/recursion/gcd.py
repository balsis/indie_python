def gcd_iter(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd(a: int, b: int) -> int:
    if b <= 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(15, 5))
print(gcd(7, 19))
