
def luhn_algorithm(number):
    numbers = str(number)[::-1]

    my_list = [i for i in numbers]

    new_list = []
    for i, v in enumerate(my_list, 1):
        if i % 2 == 0:
            if int(v) * 2 > 9:
                v = str(int(v) * 2 - 9)
            else:
                v = str(int(v) * 2)
        new_list.append(v)

    summa = 0
    for i in new_list:
        summa += int(i)
    return "True" if summa % 10 == 0 else "False"

print(luhn_algorithm(3942682966937054))
print(luhn_algorithm(2553514623369426))
