def validate_all_args(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # print(args + tuple(kwargs.values()))
            result = True
            for i in args:
                if not isinstance(i, type):
                    result = False
            if result == False:
                print(f"Все аргументы должны принадлежать типу {type}")
                return None
            else:
                return func(*args, **kwargs)

        return wrapper
    return decorator

@validate_all_args(str)
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)