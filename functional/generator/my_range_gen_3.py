def my_range_gen(*args):
    if len(args) == 1:
        n = args[0]
        i = 0
        while i < n:
            yield i
            i += 1
    elif len(args) == 2:
        start, end = args[0], args[1]
        i = start
        while i < end:
            yield i
            i += 1
    else:
        start, end, step = args[0], args[1], args[2]
        if step == 0 or (start > end and step > 0) or (start < end and step < 0):
            return
        if start < end:
            i = start
            while i < end:
                yield i
                i += step

        if end < start:
            i = start
            while i > end:
                yield i
                i += step



for i in my_range_gen(20, 10, 3):
    print(i)
print('End')
