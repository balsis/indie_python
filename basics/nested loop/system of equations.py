n, m = map(int, input().split())
count = 0
for a in range(0, 1001):
    for b in range(0, 1001):
        if a**2+b == n and a+b**2 == m:
            count+=1
print(count)