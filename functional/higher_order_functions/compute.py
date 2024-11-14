def compute(funcs: list, *args):
    return [j(i) for j in funcs for i in args]



def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([inc, dec, square], 10, 20, 30, 40))