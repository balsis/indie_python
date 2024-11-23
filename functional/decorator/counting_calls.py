from functools import wraps


def counting_calls(func):
    call_count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count +=1
        wrapper.call_count = call_count
        return func(*args, **kwargs)
    return wrapper

@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print(add.call_count)
print(add(30, 5))
print(add.call_count)





