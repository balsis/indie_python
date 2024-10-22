n, m = map(int, input().split())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

for i in range(1, n): #   строки
    for j in range(1, m): # столбцы
        matr[i][j] = matr[i-1][j]+ matr[i][j-1]
for i in matr:
    print(*i)
