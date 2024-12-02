lst = list(map(str, input().lower().split()))
result = any([i for i in lst if i.endswith('ought')])

print(result)