from functools import wraps
def add_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = ('begin',*args, 'end')
        return func(*new_args, **kwargs)
    return wrapper



@add_args
def find_max_word(*args):
    """
    Возвращает слово максимальной длины
    """
    return max(args, key=len)

print(find_max_word('my'))
print(find_max_word('my', 'how'))
print(find_max_word('my', 'how', 'maximum'))
print(find_max_word.__name__)
print(find_max_word.__doc__.strip())