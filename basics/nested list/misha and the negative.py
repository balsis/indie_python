n, m = map(int, input().split())
matr = []
negative = []
for i in range(n):
    matr.append(input())
input()
for i in range(n):
    negative.append(input())

count = 0
for i in range(n):
    for j in range(m):
        if matr[i][j] == negative[i][j]:
            count += 1
print(count)
