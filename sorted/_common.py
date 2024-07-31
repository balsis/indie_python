# сортировка по числу, если оно является частью элемента списка
a=['ZZZ 800','aaa 45','eee 43', 'DDD 800', 'BBB 43', 'www 14']
print(sorted(a, key = lambda x: int(x.split()[1]) ))

# >>> ['www 14', 'eee 43', 'BBB 43', 'aaa 45', 'ZZZ 800', 'DDD 800']



# сортировка по числу если оно является частью элемента списка, в случае если равны то стальные элементы должны быть отсортированы по алфавитному порядку. (в ламбда можно передать кортеж по нему тоже будет сортироваться
a=['ZZZ 800','aaa 45','eee 43', 'DDD 800', 'BBB 43', 'www 14']
print(sorted(a, key = lambda x: (int(x.split()[1]), x.split()[0]) ))

# >>> ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'DDD 800', 'ZZZ 800']



# то же с учётом регистра букв
a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'BBB 43', 'www 14']
print(sorted(a, key = lambda x: (int(x.split()[1]), x.split()[0].lower()) ))

# >>> ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'ddd 800', 'ZZZ 800']



# сортировка по убыванию по числу если оно является частью элемента списка, добавляем минус
a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'BBB 43', 'www 14']
print(sorted(a, key = lambda x: (-int(x.split()[1]), x.split()[0].lower()) ))

# >>> ['ddd 800', 'ZZZ 800', 'aaa 45', 'BBB 43', 'eee 43', 'www 14']


# сортировка по убыванию по числу и строке если оно является частью элемента списка, потому как добавив мину к строковой сортировке просто вызовет ошибку
a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'BBB 43', 'www 14']
print(sorted(a, key = lambda x: (int(x.split()[1]), x.split()[0].lower()) , reverse=True))

# >>> ['ZZZ 800', 'ddd 800', 'aaa 45', 'eee 43', 'BBB 43', 'www 14']



# алфавитный порядок в обратном направлении а по числам по возрастанию
a=['ZZZ 800','aaa 45','eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
a = sorted(a, key = lambda x: int(x.split()[1]) )
print(a)
a = sorted(a, key = lambda x: x.split()[0].lower(), reverse=True )
print(a)

# >>> ['aaa 14', 'eee 43', 'AaA 43', 'aaa 45', 'ZZZ 800', 'ddd 800']
# >>> ['ZZZ 800', 'eee 43', 'ddd 800', 'aaa 14', 'AaA 43', 'aaa 45']