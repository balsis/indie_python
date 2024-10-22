# Ваша задача написать функцию format_name_list, которая принимает список словарей, у каждого словаря в этом списке есть только ключ name.
# Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и".

def format_name_list(names: list):
    lst = [i['name'] for i in names]
    stt = ''
    if len(lst) == 0:
        return ''
    if len(lst) == 1:
        return lst[0]
    if len(lst) > 1:
        for i in lst[:-2]:
            stt += i + ', '
        stt += lst[-2]
        stt += ' и '
        stt += lst[-1]
        return stt
print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]))

# код ниже не стоит удалять, он нужен для проверки
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
assert format_name_list([{'name': 'Bart'}]) == 'Bart'
assert format_name_list([]) == ''
assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'

print('Проверки пройдены')