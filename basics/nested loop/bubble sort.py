n = int(input())
a = list(map(int, input().split()))
b = []*n
count = 0
for j in range(n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            count+=1
print(*a)
print(count)