lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'Добавить add-page']

menu = ()

for i in lst_in:
    name, address = i.split()
    menu += ((name, address), )

print(menu)