def add_attrs(**attribute_kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for k, v in attribute_kwargs.items():
                setattr(wrapper, k, v)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@add_attrs(hello='World', marks=[1, 2, 3], cash=100)
def add(a, b):
    return a + b

print(add(10, 5))
print(add.hello)
print(add.marks)
print(add.cash)
print(getattr(add, 'ordered', None))
