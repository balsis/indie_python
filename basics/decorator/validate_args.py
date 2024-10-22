# Напишите определение декоратора validate_args
from functools import wraps

def validate_args(func):
    @wraps(func)
    def wrapper(*args):
        if len(args) < 2:
            return 'Not enough arguments'
        if len(args) > 2:
            return 'Too many arguments'
        if not isinstance(args[0], int) or not isinstance(args[1], int):
            return 'Wrong types'
        return func(*args)
    return wrapper

# Код ниже не удаляйте, он нужен для проверки
@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


assert add_numbers(4, 5) == 9
assert add_numbers(4) == 'Not enough arguments'
assert add_numbers() == 'Not enough arguments'
assert add_numbers('hello') == 'Not enough arguments'
assert add_numbers(3, 5, 6) == 'Too many arguments'
assert add_numbers('a', 'b', 'c') == 'Too many arguments'
assert add_numbers(4.5, 5.1) == 'Wrong types'
assert add_numbers('hello', 4) == 'Wrong types'
assert add_numbers(9, 'hello') == 'Wrong types'
assert add_numbers([1, 3], {}) == 'Wrong types'
assert add_numbers.__name__ == 'add_numbers'
assert add_numbers.__doc__.strip() == 'Return sum of x and y'
print('Good')