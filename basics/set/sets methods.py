n = int(input())
all = set()
for i in range(n):
	all.update(list(map(int, input().split())))
print(len(all))