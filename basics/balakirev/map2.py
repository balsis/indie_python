s = input()
s_lst = s.split()
# house=дом car=машина men=человек tree=дерево
st = tuple(map(lambda x: tuple(x.split("=")) , s_lst))
print(st)