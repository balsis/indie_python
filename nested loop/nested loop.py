# Ваша задача найти сумму всех четырехзначных натуральных чисел, сумма цифр которых равна 20.
summa = 0
for i in range(1000, 9999, 1):
    summa2 = 0
    j = i
    while j > 0:
        summa2 += j % 10
        j //= 10
    if summa2 == 20:
        summa+=i

print(summa)