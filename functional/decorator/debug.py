# определяем декоратор
def decorator(func):
    def wrapper():  # определяем функцию, которая будет подменять поведение оригинальной
        print('Start decorator')  # вывод перед вызовом оригинальной функции
        func()  # вызов оригинальной функции
        print('Finish decorator')  # вывод после вызова оригинальной функции

    return wrapper  # возвращаем функцию, которая заменит оригинальную функцию


def say_hello():
    print('Hello world')


# декорируем функцию say_hello
say_hello = decorator(say_hello)

# вызываем say_hello
say_hello()

print('--------')


# определяем новую функцию say_bye
def say_bye():
    print('bye world')


# декорируем функцию say_bye
say_bye = decorator(say_bye)

# вызываем say_bye
say_bye()
