def print_goods(lst):
    temp = [i.split(":") for i in lst]
    for i in sorted(temp, key = lambda item: (-float(item[1]), item[0].upper())):
        print(f'{float(i[1]):.2f} - {i[0]}')


data = [
    'a: 1',
    'aa: 2',
    'aA: 3',
    'Aa: 4',
    'Aa: 5',
    'AA: 5',
    'aa: 5',
    'aA: 5',
]
print_goods(data)