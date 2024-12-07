def gen_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *=i
        yield result

for value in gen_factorial(5):
    print(value)
