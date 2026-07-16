n = int(input())
lst = []

for i in [64, 32 ,16, 8, 4, 2, 1]:
    while n >= i:
        n -= i
        lst.append(i)

print(*lst)