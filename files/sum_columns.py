def sum_columns(filename: str):
    file = open(filename)
    matrix = []
    for i in file:
        matrix.append(i.strip().split())
    lst = []
    for i in list(zip(*matrix)):
        summa = 0
        for j in i:
            summa += int(j)
        lst.append(summa)
    return lst


print(sum_columns("example.txt"))
