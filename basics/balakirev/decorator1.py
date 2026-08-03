def func_show(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        return result

    return wrapper


@func_show
def get_sq(width, height):
    return width * height


get_sq(2, 3)
