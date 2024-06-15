file = open('111.txt', 'a+', encoding='utf-8')

file.write('Hi')
print(file.read())

file.close()