file = open('numbers.txt').read()
a = file.split('\n')
a.remove('')
# print(a)
b = [int(a[i]) for i in range(len(a)) if 99 < int(a[i]) <= 999]
c = [int(a[i]) for i in range(len(a)) if 9 < int(a[i]) <= 99]
print(len(b), sum(c))
