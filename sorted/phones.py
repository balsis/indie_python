n = int(input())
dct = {}
for i in range(n):
	inp = input().split()
	dct.setdefault(inp[1], []).append(inp[0])

m = int(input())
for i in range(m):
	inp = input()
	print(*dct.get(inp, ['Неизвестный номер']))

