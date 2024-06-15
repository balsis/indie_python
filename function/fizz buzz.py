# Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка.
# Функция generate_fizz_buzz_list должна:
# обойти числа от 1 до n включительно и для каждого такого числа выполнить последовательно проверки с пункта 2 по пункт 5
# Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz
# Если число кратно трем, то в список заносим строку Fizz
# Если число кратно пяти, то в список заносим строку Buzz
# Если число не кратно ни трем ни пяти, то в список заносим само это число
# В итоге функция generate_fizz_buzz_list должна вернуть сформированный список из n элементов

def generate_fizz_buzz_list2(n):
    return ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, n+1)]

def generate_fizz_buzz_list(n):
    lst = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append('FizzBuzz')
        elif i % 3 == 0:
            lst.append('Fizz')
        elif i % 5 == 0:
            lst.append('Buzz')
        else:
            lst.append(i)
    return lst
print(generate_fizz_buzz_list(4))
