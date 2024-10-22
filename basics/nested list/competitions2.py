n, m = map(int, input().split())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

maxim, x, y = 0, 0, 0

for i in range(n):
    for j in range(m):
        if maxim < matr[i][j]:
            maxim = matr[i][j]
            x, y = i, j
print(maxim)
print(x, y, sep=' ')