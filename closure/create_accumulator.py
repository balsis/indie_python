def create_accumulator():
    summa = 0
    def inner (value):
        nonlocal summa
        summa += value
        return summa
    return inner

summator_1 = create_accumulator()
print(summator_1(1)) # печатает 1
print(summator_1(5)) # печатает 6
print(summator_1(2)) # печатает 8