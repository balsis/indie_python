def first_validator(func):
    def my_wrapper(*args, **kwargs):
        print(f"Начинаем важную проверку")
        if len(args) == 3:
            func(*args, **kwargs)
        else:
            print(f"Важная проверка не пройдена")
            return None
        print(f"Заканчиваем важную проверку")

    return my_wrapper


def second_validator(func):
    def my_wrapper(*args, **kwargs):
        print(f"Начинаем самую важную проверку")
        if kwargs.get('name') == 'Boris':
            func(*args)
        else:
            print(f"Самая важная проверка не пройдена")
            return None
        print(f"Заканчиваем самую важную проверку")

    return my_wrapper


# используйте декораторы
@second_validator
@first_validator
def sum_values(*args):
    print(f'Получили результат равный {sum(args)}')

sum_values(70,6,1,name="Boris")
# вызовите функцию sum_values()