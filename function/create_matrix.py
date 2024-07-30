
def create_matrix(size = 3, up_fill = 0 , down_fill = 0):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = i + 1
            elif i < j:
                matrix[i][j] = up_fill
            else:
                matrix[i][j] = down_fill
    return matrix


assert create_matrix() == [[1, 0, 0],
                           [0, 2, 0],
                           [0, 0, 3]]
assert create_matrix(4) == [[1, 0, 0, 0],
                            [0, 2, 0, 0],
                            [0, 0, 3, 0],
                            [0, 0, 0, 4]]
assert create_matrix(up_fill=7) == [[1, 7, 7],
                                    [0, 2, 7],
                                    [0, 0, 3]]
assert create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7],
                                                 [9, 2, 7],
                                                 [9, 9, 3]]
assert create_matrix(size=4, up_fill=7, down_fill=9) == [[1, 7, 7, 7],
                                                         [9, 2, 7, 7],
                                                         [9, 9, 3, 7],
                                                         [9, 9, 9, 4]]