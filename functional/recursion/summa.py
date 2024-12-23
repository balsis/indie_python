def summa(n):
    if n == 1:
        return 1
    return summa(n - 1) + n


print(summa(4))
