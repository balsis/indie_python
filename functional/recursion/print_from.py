def print_from(n):
    while n > 0:
        print(n)
        return print_from(n-1)


print_from(2)
