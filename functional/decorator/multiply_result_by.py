def multiply_result_by(n):
    def decorator(original_function):
        def wrapper(*args, **kwargs):
            return (original_function(*args, **kwargs)) * n
        return wrapper
    return decorator


@multiply_result_by(2)
def my_function(x, y):
    return x + y

print(my_function(5, 6))



@multiply_result_by(3)
@multiply_result_by(4)
def my_function(x, y):
    return x + y


print(my_function(2, 3))