n, m = map(int, input().split())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

# print(matr)
maxim = 0
number = 0
for i in range(n):
    summa = 0
    for j in range(m):
        summa += matr[i][j]
    # print(summa)
    if maxim < summa:
        maxim = summa
        number = i
print(maxim, number, sep='\n')
