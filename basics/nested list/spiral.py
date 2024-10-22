n = int(input())           # ввод размера матрицы
a = []
for i in range(n):         # создание нулевой матрицы
    a.append([0] * n)
count = 1                  # счетчик
a[n // 2][n // 2] = n * n  # центральный элемент

for i in range(n // 2):             # определяем количество витков
    for j in range(i, n - i):       # идем по матрице вправо
        a[i][j] = count
        count += 1
    for j in range(i + 1, n - i):   # идем по матрице вниз
        a[j][n-1-i] = count
        count += 1
    for j in range(n-2-i,-1+ i,-1): # идем по матрице влево
        a[n-1-i][j] = count
        count += 1
    for j in range(n-2-i,i,-1):     # идем по матрице вверх
        a[j][i] = count
        count += 1

# выводим матрицу
for i in a:
    print(*i)