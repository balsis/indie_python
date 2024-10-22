# Напишите определение декоратора add_args
def add_args(func):
    def wrapper(*args, **kwargs):
        modified_args = ('begin', *args, 'end')
        return func(*modified_args, **kwargs)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

# Код ниже не удаляйте, он нужен для проверки
@add_args
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


@add_args
def find_max_word(*args):
    """
    Возвращает слово максимальной длины
    """
    return max(args, key=len)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
assert concatenate('hello', 'world', 'my', 'name is', 'Artem') == 'begin, hello, world, my, name is, Artem, end'
assert concatenate('my', 'name is', 'Artem') == 'begin, my, name is, Artem, end'
assert concatenate.__name__ == 'concatenate'
assert concatenate.__doc__.strip() == """Возвращает конкатенацию переданных строк"""
assert find_max_word('my') == 'begin'
assert find_max_word('my', 'how') == 'begin'
assert find_max_word('my', 'how', 'maximum') == 'maximum'
assert find_max_word.__name__ == 'find_max_word'
assert find_max_word.__doc__.strip() == """Возвращает слово максимальной длины"""