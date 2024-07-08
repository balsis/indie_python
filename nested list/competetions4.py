n, m = map(int, input().split())
matr = [list(map(int, input().split())) for _ in range(n)]
lst = []

for i in range(n):
    athlete_max = max(matr[i])
    lst.append(athlete_max)

print(lst.count(max(lst)))


