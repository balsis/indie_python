def compute(funcs_list, *args):
    lst = []
    for i in args:
        num = i
        for func in funcs_list:
            num = func(num)
        lst.append(num)
    return lst


def inc(num):
    return num + 1

def dec(num):
    return num - 1

def repeater(value, n=3):
    return str(value) * n

def square(num):
    return num ** 2

print(compute([dec, inc, square, repeater], 5, 7, 0, True))
