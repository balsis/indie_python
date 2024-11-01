def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    matr = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            if i == j:
                row.append(i)
            elif i < j:
                row.append(up_fill)
            else:
                row.append(down_fill)
        matr.append(row)
    return matr


print(create_matrix())
