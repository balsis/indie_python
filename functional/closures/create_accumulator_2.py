def create_accumulator(start=0):
    summa = start

    def inner(x):
        nonlocal summa
        summa += x
        return summa

    return inner


summator_1 = create_accumulator(200)
print(summator_1(5))
print(summator_1(7))
print(summator_1(2))

summator_2 = create_accumulator()
print(summator_2(3))
print(summator_2(6))