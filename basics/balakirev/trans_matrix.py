lst_in = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [5, 4, 3]]

rows = len(lst_in) # строки
cols = len(lst_in[0]) # столбцы

print(rows)
print(cols)

lst_out = [[lst_in[j][i] for j in range(rows)] for i in range(cols)]
print(lst_out)