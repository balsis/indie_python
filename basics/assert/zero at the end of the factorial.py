def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    a = factorial(n)
    count = 0
    a = str(a)
    for i in range(len(a)-1, 0, -1):
        if a[i] != '0':
            break
        count += 1
    return count
# print(trailing_zeros(20))

# код ниже не стоит удалять, он нужен для проверки
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Проверки пройдены')