def multiply(*args):
    result = 1
    for i in args:
        result *=i
    return result

print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10))
print(multiply(1, 2, 3, 4, 5, 6))
