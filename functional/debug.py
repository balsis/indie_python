my_list = [
    (10, 10, 10),
    (8, 10, 12),
    (6, 12, 9),
    (10, 12, 14)
]
s = sorted(my_list, key=lambda x: (-x[0], -x[2]))
print(*s, sep='\n')