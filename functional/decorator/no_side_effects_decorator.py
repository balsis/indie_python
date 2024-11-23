from functools import wraps


def no_side_effects_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(args[0].copy(),*args[1:],**kwargs)

    return wrapper


@no_side_effects_decorator
def add_element(data, element):
    data.append(element)
    return data


my_list = [1, 2, 3]
print('Результат вызова =', add_element(my_list, 4))
print('Результат вызова =', add_element(my_list, 5))
print(my_list)
print(add_element.__name__)
