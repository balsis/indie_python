def convert_to(type_):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return type_(func(*args, **kwargs))

        return wrapper

    return decorator


@convert_to(str)
def add_values(a, b):
    return a + b


result = add_values(10, 20)
print(f"Результат: {result}, тип результата {type(result)}")


@convert_to(list)
def add_values(a, b):
    return a + b


result = add_values('hello', 'world')
print(f"Результат: {result}, тип результата {type(result)}")
