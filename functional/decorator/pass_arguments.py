def pass_arguments(*args_add, **kwargs_add):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, *args_add, **kwargs, **kwargs_add)
        return wrapper
    return decorator


@pass_arguments(1, 2, 3)
def add(*values):
    return sum(values)


print(add(5, 4, 6))