def create_accumulator(first=0):
    summa = first
    def inner (value):
        nonlocal summa
        summa += value
        return summa
    return inner

summator_1 = create_accumulator(100)
print(summator_1(1)) # печатает 101
print(summator_1(5)) # печатает 106
print(summator_1(2)) # печатает 108