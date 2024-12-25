def get_arith_progression(a1, d, n):

    if n == 1:
        return a1
    if n == 2:
        return a1 + d
    else:
        return d + get_arith_progression(a1, d, n-1)

print(get_arith_progression(4, 2, 3))
print(get_arith_progression(10, -3, 5))
print(get_arith_progression(100, -8, 11))
