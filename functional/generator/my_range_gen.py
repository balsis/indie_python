def my_range_gen(n):
    i = 0
    while i < n:
        yield i
        i += 1


for value in my_range_gen(5):
    print(value)
