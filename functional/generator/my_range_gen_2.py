def my_range_gen(a=0, b=None):
    i = a
    while i < b:
        yield i
        i += 1


for value in my_range_gen(5):
    print(value)
