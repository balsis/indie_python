from functools import wraps
def upper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """
        Внутренняя функция декоратора
        """
        return func(*args, **kwargs).upper()
    return inner


@upper
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)

print(concatenate.__name__)
print(concatenate.__doc__.strip())