values = [('bb', 80), ('aa', 45), ('Bb', 5), ('ss', 43), ('AA', 80), ('BB', 8), ('Aa', 14)]
print(values)
# отсортируем все значения по возрастанию чисел
temp_list = sorted(values, key=lambda x: int(x[1]))
print(temp_list)
# расположить элементы против алфавитного порядка,
# причем в пределах группы с одинаковым строковым значением элементы не будут меняться местами.
# Они уже выстроены в нужном нам порядке после первого этапа
new_list = sorted(temp_list, key=lambda x: x[0].lower(), reverse=True)

print(new_list)
# Теперь все элементы расположены по убыванию алфавитного порядка и возрастанию числового порядка вторых элементов.

dc = {'makron78', 'realdonaldtrump', 'joebiden'}
print(len(dc))


print(type(dict))