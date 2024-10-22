# Напишите функцию count_letter(text, letter), которая принимает два параметра:
#
# text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
# letter – буква, количество которой мы должны посчитать в text.
# Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text
# Ваша задача дописать только тело функции count_letter

# объявление функции
def count_letter(text, letter):
    print(text.count(letter))
# считываем данные
text = input()
symbol = input()
# вызываем функцию
count_letter(text, symbol)