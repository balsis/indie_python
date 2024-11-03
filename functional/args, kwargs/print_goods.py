def print_goods(*args):
    number = 0
    for i in args:
        if isinstance(i, str) and len(i)>0:
            number += 1
            print(f"{number}. {i}")
    if number == 0:
        print("Нет товаров")


print_goods('apple', 'banana', 'orange')
print_goods(1, True, 'Грушечка', '', 'Pineapple')
print_goods([], {}, 1, 2)
