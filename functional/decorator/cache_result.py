from functools import wraps


def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            print(f'[FROM CACHE] Вызов {func.__name__} = {cache[args]}')
            return cache[args]
        else:
            cache[args] = func(*args, **kwargs)
            return func(*args, **kwargs)
    return wrapper


@cache_result
def add(a, b):
    return a + b

print(add(4, 4)) # 1й раз с такими атрибутами
print(add(4, 5)) # 1й раз с такими атрибутами
print(add(4, 6)) # 1й раз с такими атрибутами
print(add(4, 5)) # достаем из кеша
print(add(5, 4)) # 1й раз с такими атрибутами
print(add(6, 3)) # 1й раз с такими атрибутами
print(add(a=6, b=3)) # 1й раз с такими атрибутами: позицицинные!=именованные
print(add(a=6, b=3)) # достаем из кеша
