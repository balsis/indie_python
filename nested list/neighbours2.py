n, m = map(int, input().split())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

for i in range(n-2, -1, -1): #   строки
    for j in range(m-2, -1, -1): # столбцы
        matr[i][j] = matr[i+1][j] + matr[i][j+1]
for i in matr:
    print(*i)
