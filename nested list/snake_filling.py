n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        print(*list(range(m*i, m*i+m)))
    else:
        print(*list(range(m*i+m-1, m*i-1, -1)))

