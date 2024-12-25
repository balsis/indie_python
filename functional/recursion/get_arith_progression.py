def get_arith_progression(n):
    step = 7
    if n == 1:
        return 1
    if n == 2:
        return 1 + step
    else:
        return step + get_arith_progression(n-1)

print(get_arith_progression(4))
