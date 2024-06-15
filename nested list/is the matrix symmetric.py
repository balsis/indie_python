# Проверьте, является ли двумерный массив симметричным относительно главной диагонали.
# Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.

n = int(input())
matr = []
flag = True
for i in range(n):
    matr.append(list(map(int, input().split())))

for i in range (n):
    for j in range(n):
        if matr[i][j] != matr [j][i]:
            flag = False
else:
    if flag == True:
        print('Yes')
    else:
        print('No')