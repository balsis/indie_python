n, m = map(int, input().split())
color = "C" or "M" or "Y"
matr = []
for i in range(n):
    matr.append(list(map(str, input().split())))
mark = 0

for i in range(n):
    for j in range(m):
        if "C" in matr[i][j] or "M" in matr[i][j] or "Y" in matr[i][j]:
            mark = 1


print("#Color" if mark == 1 else "#Black&White")
