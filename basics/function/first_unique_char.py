# Напишите функцию first_unique_char, которая принимает строку символов и возвращает целое число:
# позицию первого уникального символа в строке. В случае, если уникальных символов в переданной строке нет, верните -1.
# Регистр символов не учитывайте.
# Ваша задача написать только определение функции first_unique_char

def first_unique_char(string):
    lst = [i for i in string if string.count(i) == 1]
    return string.find(lst[0]) if len(lst) >= 1 else -1

print(first_unique_char('aasssddddddddq'))