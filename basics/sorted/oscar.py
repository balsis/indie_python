
lst = [input() for i in range(int(input()))]
dct = {i: lst.count(i) for i in lst}

sorted_dct = sorted(dct.items(), key= lambda x: x[1], reverse=True)

print(*sorted_dct[0], sep=', ')
print(*sorted_dct[len(dct)-1], sep=', ')