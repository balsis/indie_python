# ввод значения N (эту переменную не менять)
N = int(input())

def get_sum(total):
    summa = 0
    for i in range(1, total+1):
        summa += i
        yield summa


gen = get_sum(N)
print(next(gen))
print(next(gen))
print(next(gen))


