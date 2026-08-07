from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sum(res)

    return wrapper


@decorator
def get_list(st: str):
    """Функция для формирования списка целых значений"""
    return list(map(int, st.split()))


print(get_list("1 2 3"))