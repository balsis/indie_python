n, x = map(int, input().split())

table = []
for i in range(1, n+1):
    for j in range(1, n+1):
        table.append(i*j)

print(table.count(x))

