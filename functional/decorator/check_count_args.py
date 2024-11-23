from functools import wraps
def check_count_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        count_args = len(args)+len(kwargs)
        if count_args ==2:
            return func(*args, **kwargs)
        elif count_args < 2:
            return(print("Not enough arguments"))
        else:
            return(print("Too many arguments"))

    return wrapper


@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y

add_numbers(3, 5, 6)