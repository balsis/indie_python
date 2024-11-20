def replace(f):
    def wrapper(*args, **kwargs):
        print('Функция задекорирована')
        f(*args)

    return wrapper


@replace
def my_function(*args, **kwargs):
    print(f"Запустили функцию с {args=} и {kwargs=}")


my_function(1, 2, 3, a=10, b=20)