def my_enumerate(lst, start=0):
    for i in range(len(lst)):
        yield i+start, lst[i]

lessons = ["Что такое функция", "Возвращаемое значение",
           "Параметры и аргументы функции",
           "Чистая функция", "Параметр *args"]

for i, lesson in my_enumerate(lessons):
    print("Урок {}: {}".format(i, lesson))