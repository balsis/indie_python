a = [1, 2, 3]
b = {1: 100, 2: 200}
try:
    print(a[5])
    print(b[4])
    print(7 / 0)
except KeyError:
    print('Плохой ключ')
except IndexError:
    print('Плохой индекс')
except ZeroDivisionError:
    print('Не делите на 0!')