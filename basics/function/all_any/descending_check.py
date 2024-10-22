a = list(map(int, input().split()))
b = sorted(a, reverse=True)
print(True if a==b and len(set(a)) > 1 else False)