n, m = map(int, input().split())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

maxim, x,  = 0, 0
winner_summa = 0
winner_max = 0
for i in range(n):
    summa = 0
    athlete_maximum = 0

    for j in range(m):
        summa += matr[i][j]
        # находим максимум по каждому
        if athlete_maximum < matr[i][j]:
            athlete_maximum = matr[i][j]
            #print(f'атлет {i}, попытка {j}, максимум - {athlete_maximum}')
    if winner_max < athlete_maximum:
        winner_summa = summa
        winner_max = athlete_maximum
        x = i
    elif winner_max == athlete_maximum:
        if winner_summa < summa:
            winner_summa = summa
            x = i
    #print(f'атлет {i} - максимальное значение {athlete_maximum}, всего набрал {summa}, максимум победителя {winner_max}, сумма победителя {winner_summa}')

print(x)
