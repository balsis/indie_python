def apply(func, it):
    return [func(i) for i in it]


def square(num):
    return num ** 2


print(apply(square, [5, 7, 0, 3]))