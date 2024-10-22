def print_from(n: int):
    if n > 0:
        print(n)
        print_from(n - 1)


print_from(4)
