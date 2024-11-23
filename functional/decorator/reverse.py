from functools import wraps

def reverse(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = tuple(reversed(args))
        return func(*new_args)
    return wrapper


@reverse
def get_max_index(*args):
    if not args:
        return None
    max_index = 0
    for i in range(len(args)):
        if args[i] > args[max_index]:
            max_index = i
    return max_index


print(get_max_index(1, 2, 3, 4, 5))
print(get_max_index(3, 4, 1, 5, 2))
print(get_max_index(5, 3, 4, 1, 2))
print(get_max_index.__name__)

