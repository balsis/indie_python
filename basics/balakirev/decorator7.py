s = input()


def decorator_with_param(tag: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f'<{tag}>{res}</{tag}>'

        return wrapper

    return decorator


@decorator_with_param(tag="div")
def transformation(st: str):
    return st.lower()


res = transformation(s)
print(res)
