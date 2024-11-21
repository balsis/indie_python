def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        # print(args + tuple(kwargs.values()))
        result = True
        for i in args:
            if not isinstance(i, str):
                result = False
        if not result:
            print("Все аргументы должны быть строками")
            return None
        else:
            return func(*args, **kwargs)

    return wrapper

def validate_all_kwargs_int_pos(func):
    def wrapper(*args, **kwargs):
        result = True
        for i in kwargs.values():
            if not isinstance(i, int):
                result = False
            elif isinstance(i, int) and i <= 0:
                result = False
        if not result:
            print("Все именованные аргументы должны быть положительными числами")
            return None
        else:
            return func(*args, **kwargs)
    return wrapper

@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate(a="i", b='Love', c="Python"))


@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate(a=10, b=20, c=50))


@validate_all_args_str
@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result

print(concatenate('Hello', 2, 'World', a="i", b='Love', c="Python"))