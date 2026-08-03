menu = input()


def show_menu(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i, value in enumerate(result, start=1):
            print(f"{i}. {value}")
        return result

    return wrapper


@show_menu
def get_menu(s):
    return s.split()


get_menu(menu)