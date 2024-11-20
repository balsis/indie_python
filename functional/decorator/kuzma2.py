
def decorator(func):
    def wrapper(*args, **kwargs):
        print('---Start calculation---')
        result = func(*args, **kwargs)
        print(f'---Finish calculation. Result is {result}---')
        return result
    return wrapper



@decorator
def add(*values):
    return sum(values)

add(1, 4, 5, 6)


@decorator
def add_with_factor(*values, factor=1):
    return sum(values) * factor


add_with_factor(1, 4, 5, 6, factor=2)


@decorator
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


concatenate(a = "Я", b = "Выучу", c = "Этот", d = "Питон", e = "!")