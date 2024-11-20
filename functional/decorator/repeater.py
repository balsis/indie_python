def repeater(func):
    def wrapper(*args, **kwargs):
        [func(*args, **kwargs) for _ in range(3)]

    return wrapper


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(9, 4)
