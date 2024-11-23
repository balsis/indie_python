from functools import wraps
def explicit_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args != ():
            print("Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений")
        else:
            return func(**kwargs)

    return wrapper

@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, 20))


@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(a=10, b=20))


@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add.__name__)
print(add.__doc__)