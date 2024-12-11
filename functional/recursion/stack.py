def first_func():
    a, b = 10, 20
    print(a, b, id(a), id(b))
    second_func()

def second_func():
    a, b = 30, 40
    print(a, b, id(a), id(b))
    third_func()

def third_func():
    a, b = 50, 60
    print(a, b, id(a), id(b))

first_func()