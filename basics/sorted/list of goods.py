# Sony PlayStation 5: 46000
# Телевизор QLED Samsung QE65Q60TAU: 87090
# Смартфон Samsung Galaxy A11: 10000
# Планшет Samsung Galaxy Tab S6: 26600
# конец
lst = []
while True:
    a = input()
    if a == 'конец':
        break
    lst.append(a.split(':'))

a = sorted(lst, key = lambda x: int(x[1]), reverse= True)
for i in a:
    print(i[0])