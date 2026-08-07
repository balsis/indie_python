s = input()


def decorator_with_start_value(start):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res + start

        return wrapper

    return decorator

@decorator_with_start_value(start=5)
def my_func(value: str):
    return sum(map(int, value.split()))


print(my_func(s))
