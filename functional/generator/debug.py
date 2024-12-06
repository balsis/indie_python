def get_names():
    print('Start')
    print('Continue')
    yield 'Тинки-Винки'
    print('Continue - 2')
    print('Continue - 3')
    yield 'Дипси'
    print('Continue - 4')
    yield 'Ляля'
    print('Continue - 5')
    yield 'По'

result = get_names()
print(result)
print(next(result))
print('---------')
print(next(result))
print('---------')
print(next(result))
print('---------')
print(next(result))