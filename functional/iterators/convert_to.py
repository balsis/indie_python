def convert_to(values, type_to=int):
    return list(map(type_to, values))



numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150]
print(convert_to(numbers, str))


numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150]
print(convert_to(numbers, float))

numbers = ['-383', '-101', '121', '40', '278', '118', '-462']
print(convert_to(numbers))