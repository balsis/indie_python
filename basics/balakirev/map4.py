lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']

lst2D_check = [[8, 11, -5], [3, 4, 10], [-1, -2, 3], [4, 5, 6]]


lst2D = list(map(lambda x: list(map(int, x.split())), lst_in))


print(lst2D)
assert lst2D == lst2D_check