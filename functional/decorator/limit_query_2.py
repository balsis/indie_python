from functools import wraps


def limit_query(limit):
    def decorator(func):
        total_calls = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal total_calls
            if total_calls < limit:
                total_calls += 1
                return func(*args, **kwargs)
            else:
                print(f"Лимит вызовов закончен, все {limit} попытки израсходованы")

        return wrapper

    return decorator


@limit_query(3)
def add(a: int, b: int):
    return a + b


print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)
