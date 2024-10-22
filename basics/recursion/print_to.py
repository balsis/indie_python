def print_to(n):
    if n == 0:
        return
    print_to(n-1)
    print(n)

print_to(5)