a = []
for i in range(4):
    a.append(input())
flag = True
for i in range(4 - 1):
    for j in range(4 - 1):
        if a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1]:
            flag = False
print("No") if flag == False else print("Yes")
