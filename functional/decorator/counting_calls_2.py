from functools import wraps


def counting_calls(func):
    call_count = 0
    calls = []
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count +=1
        calls.append({
            "args": args,
            "kwargs": kwargs
        })
        wrapper.call_count = call_count
        wrapper.calls= calls
        return func(*args, **kwargs)
    return wrapper


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print('Количество вызовов =', add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])