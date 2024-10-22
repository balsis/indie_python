# Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# middlename– отчество человека;
# а затем выводит на печать фамилию и инициалы в определенном формате (первая буква фамилии должна стать заглавной, все остальные строчные; в имени и отчестве остаются только по одной букве в верхнем регистре).
# Ваша задача дописать только тело функции print_initials

# объявление функции
def print_initials(name, surname, middlename):
    print(f'{surname.capitalize()} {name[0].upper()}.{middlename[0].upper()}.')

# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)