def gen_fibonacci_numbers(n):
    a, b = 1, 1
    for i in range(1, n+1):
        yield a
        a, b = b, a + b


for i in gen_fibonacci_numbers(5):
    print(i)