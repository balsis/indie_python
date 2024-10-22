def print_goods(*args):
    lst = [i for i in args if isinstance(i, str) and len(i) > 0 and i != ' ']
    # print(lst)
    if len(lst) == 0:
        print('Нет товаров')
    else:
        for i in range(len(lst)):
            print(f'{i+1}. {lst[i]} ')

print_goods('apple', 'banana', 'orange')