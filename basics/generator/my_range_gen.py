def my_range_gen(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    if len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
    if step < 0:
        while i > stop:
            yield i
            i += step


# tests
assert ([i for i in my_range_gen(5)]) == [i for i in range(5)]
assert ([i for i in my_range_gen(4,8)]) == [i for i in range(4,8)]
assert ([i for i in my_range_gen(4, 8, 2)]) == [i for i in range(4, 8, 2)]
assert ([i for i in my_range_gen(8, 5, -1)]) == [i for i in range(8, 5, -1)]
assert ([i for i in my_range_gen(20, 10, 3)]) == [i for i in range(20, 10, 3)]
assert ([i for i in my_range_gen(1, 10, -2)]) == [i for i in range(1, 10, -2)]

for i in my_range_gen(4, 8):
    print(i)


