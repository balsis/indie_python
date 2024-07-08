n, m = map(int, input().split())
matr = [list(map(int, input().split())) for _ in range(n)]

winner_index = 0
winner_sum = 0
winner_max = 0

for i in range(n):
    athlete_sum = sum(matr[i])
    athlete_max = max(matr[i])

    if athlete_max > winner_max or (athlete_max == winner_max and athlete_sum > winner_sum):
        winner_index = i
        winner_sum = athlete_sum
        winner_max = athlete_max

print(winner_index)