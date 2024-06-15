# Напишите функцию repeat_please_n_times, которая принимает один аргумент n - натуральное число.
# Функция repeat_please_n_times должна n раз распечатать фразу "Just do it" в отдельной строчке
# Ваша задача написать только определение функции repeat_please_n_times, вызывать ее не нужно

def repeat_please_n_times(n):
    for i in range(n):
        print("Just do it")

repeat_please_n_times(5)
