def gen_odd(n):
    for i in range(1, n+1, 2):
        yield i

for value in gen_odd(5):
    print(value)