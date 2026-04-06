def sum_columns(filename: str):
    file = open(filename)
    matrix = []
    for i in file:
        matrix.append(i.strip().split())
    lst = []
    for i in range(len(matrix)):
        summa = 0
        for j in range(len(matrix[i])):
            print(i, j, matrix[i][j])
            summa += int(matrix[i][j])
        lst.append(summa)
    return lst


print(sum_columns("example.txt"))
