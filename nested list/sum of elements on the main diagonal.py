# Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.
# Под главной диагональю матрицы подразумевается диагональ, проведённая из левого верхнего угла в правый нижний.

n = int(input())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))
# print(matr)
summa = 0
for i in range(n):
    for j in range(n):
        if i == j:
            summa += matr[i][j]
print(summa)
