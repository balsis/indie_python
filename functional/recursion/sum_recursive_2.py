def sum_recursive(lst):
    summa = 0
    for i in lst:
        if isinstance(i, list):
            summa += sum_recursive(i)
        elif isinstance(i, int):
            summa += i
    return summa

print(sum_recursive([1, 2, 3, 4, 5]))
print(sum_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
