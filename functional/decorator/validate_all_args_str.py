def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        # print(args + tuple(kwargs.values()))
        result = True
        for i in args:
            if not isinstance(i, str):
                result = False
        if result == False:
            print("Все аргументы должны быть строками")
            return None
        else:
            return func(*args, **kwargs)

    return wrapper


# @validate_all_args_str
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
#
#
# @validate_all_args_str
# def concatenate(**kwargs):
#     result = ""
#     for arg in kwargs.values():
#         result += str(arg)
#     return result
#
#
# print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
#
# @validate_all_args_str
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# print(concatenate("Через", 9, "Месяцев"))


@validate_all_args_str
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "думаю", "Выучить", "Питон", a="За", b=10, c="Месяцев"))