def filter_even(func):
    def wrapper(*args, **kwargs):
        def check(index):
            if isinstance(index, int):
                return index % 2 == 0
            elif isinstance(index, (str, list, tuple, dict)):
                return len(index) % 2 == 0
            return False

        new_args = tuple(i for i in args if check(i))
        return func(*new_args, **kwargs)

    return wrapper


def delete_short(func):
    def wrapper(*args, **kwargs):
        new_kwargs = {k: v for k, v in kwargs.items() if len(k) > 4}
        return func(*args, **new_kwargs)
    return wrapper


@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))