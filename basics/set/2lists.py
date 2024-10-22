a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = set(a).difference(set(b))
print(*sorted(list(c)))
