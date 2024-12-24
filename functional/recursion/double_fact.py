def double_fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * double_fact(n - 2)


print(double_fact(6))
