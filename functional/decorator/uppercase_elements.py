def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            return [i.upper() if isinstance(i, str) else i for i in res]
        elif isinstance(res, dict):
            return {k.upper() if isinstance(k, str) else k: v for k, v in res.items()}

    return wrapper


@uppercase_elements
def my_func():
    return ['monarch', 'Touch', 'officiaL', 'DangerouS', 'breathe']


print(my_func())


@uppercase_elements
def my_func(name, surname):
    return ['temple', 'store', name, surname, *[1, 2, 3]]


print(my_func('Gerard', 'Pique'))


@uppercase_elements
def my_func(**kwargs):
    return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs


print(my_func(**{'Five': 5, 'sIx': 6}))
